import logging
import sys
import json
from flask_douwa import routes
from flask_douwa.rpc.generator_id import GeneratorRpc
from flask_douwa.rpc.demo import ProxyGetRpc
# from flask_douwa.cache import RedisCache
from flask_douwa.rpc_client.greeter_client import run
import _thread as thread
from flask_douwa import kafka_broker
import ssl
import socket
from kafka import KafkaProducer, KafkaConsumer,TopicPartition
from kafka.errors import KafkaError



"""
start 从阿里demo抄的
"""
# context = ssl.create_default_context()
# context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
# context.verify_mode = ssl.CERT_REQUIRED

# # context.check_hostname = True
# context.load_verify_locations("ca-cert")

"""
end 从阿里demo抄的
"""


# redis = RedisCache()
logger = logging.getLogger(__name__)


class Douwa(object):
    client_access = list()

    def __init__(self, app=None):
        self.getid = None
        self.kafka_callback = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        host = app.config.get("GENERATORID_IP", None)
        # r_host = app.config.get("REDIS_HOST", None)
        # r_port = app.config.get("REDIS_PORT", None)
        # r_db = app.config.get("REDIS_DB", None)
        # r_pwd = app.config.get("REDIS_PWD", None)
        key_url = app.config.get("KEY_URL")
        self.oauth_rpc_host = app.config.get("OAUTH_RPC_HOST")
        # print("oauth_rpc_host:%s" % self.oauth_rpc_host)

        if not host:
            logger.error("GENERATORID_IP:随机id生成器服务器地址没有配置")
            sys.exit(0)
        # if not r_host:
        #     logger.error("REDIS_HOST:没有配置REDIS HOST")
        #     sys.exit(0)
        # if not r_port:
        #     logger.error("REDIS_PORT:没有配置REDIS PORT")
        #     sys.exit(0)
        # if not r_db:
        #     logger.error("REDIS_DB:没有配置REDIS DATABASE NAME")
        #     sys.exit(0)
        if not key_url:
            logger.error("KEY_URL: 没有配置KEY_URL")
            sys.exit(0)

        # 随机生成id
        rpc_register = routes.register
        proto = rpc_register(GeneratorRpc)
        self.getid = ProxyGetRpc(host, proto[0], GeneratorRpc.name)


        # REDIS连接
        # redis.connect(r_host, r_port, r_db, r_pwd)

        # access_token 设置永久1个月token时间
        Douwa.client_access = app.config.get("ACCESS_TOKEN", list())

        # kafka 设置
        self.consumer_pid = app.config.get("CONSUMER_PID")
        self.conf = dict()
        self.conf["bootstrap.servers"] = app.config.get("KAFKA_HOST")
        self.conf['retries'] = app.config.get("KAFKA_RETRIES", 5)

        # self.conf['sasl.mechanisms'] = "PLAIN"
        # self.conf['security.protocol'] = 'SASL_SSL'
        # self.conf["ssl.ca.location"] = app.config.get("SSL_PATH")
        # self.conf['sasl.username'] = app.config.get("KAFKA_USERNAME")
        # self.conf['sasl.password'] = app.config.get("KAFKA_PASSWORD")

        self.topic = app.config.get("TOPIC", None)
        """start kafka相关的东西"""

        if self.topic and self.conf["bootstrap.servers"]:
            from flask_douwa import kafka_broker

            if not self.kafka_callback:
                logging.error("启动kafka错误 没有监视函数")
                return
            logging.info("启动kafka consumter 服务")
            thread.start_new(kafka_broker.read_notification_from_ceilometer_over_kafka,
                             (self.conf, self.topic, self.consumer_pid, self.kafka_callback))

        else:
            """使用的是kafka-python 包"""
            default_setting_producer = {
                "sasl_mechanism": "PLAIN",
                # "ssl_context": context,
                # "security_protocol": "SASL_SSL",
                "retries": 5
            }
            default_setting_consumer = {
                "sasl_mechanism": "PLAIN",
                # "ssl_context": context,
                # "security_protocol": "SASL_SSL"
            }

            self.kafka_setting_producer = app.config.get("KAFKA_SETTING_PORDUCER")
            if self.kafka_setting_producer:
                self.topic_name_producer = self.kafka_setting_producer.pop("topic_name")
                self.kafka_setting_producer.update(default_setting_producer)
                self.producer = KafkaProducer(**self.kafka_setting_producer)
                self.producer.partitions_for(self.topic_name_producer)

            self.kafka_setting_consumer = app.config.get("KAFKA_SETTING_CONSUMER")
            if self.kafka_setting_consumer:
                self.topic_name_consumer = self.kafka_setting_consumer.pop("topic_name")
                # tp = TopicPartition(self.topic_name_consumer, 1)
                self.kafka_setting_consumer.update(default_setting_consumer)
                self.consumer = KafkaConsumer(**self.kafka_setting_consumer)
                # self.consumer.assign([tp])
                self.consumer.subscribe(self.topic_name_consumer)
            """使用的是kafka-python 包"""

    def send_message(self, message,key=None):
        if self.topic and self.conf["bootstrap.servers"]:
            kafka_broker.send_message(self.conf, self.topic, message)
            return True
        elif self.kafka_setting_producer:
            try:
                future = self.producer.send(self.topic_name_producer, message,key=key)
                future.get()
                return True
            except KafkaError as e:
                logger.error(e)
                return False
        else:
            logger.error("kafka配置错误")
            return False

    def generator_id(self):
        if self.getid:
            return self.getid.GeneratorId()
        else:
            raise Exception("没有初始化")

    def get_message(self, data, arg):
        from flask_douwa.rpc_client.rpc_permission import rpc_permission_verify
        #去除掉权限
        if arg == "user" or arg == "group" or arg == "group_list" or arg == "user_list" or data.get('tenant_id'):
            return run(self.oauth_rpc_host, data, arg)
        user = None
        if data.get('key'):
            # key_prefix = "douwa:key:"
            # key = key_prefix + data.get('key')
            # user_cached = redis.get(key)
            user_cached = run(self.oauth_rpc_host, data, "user")
            if user_cached:
                userrole_dd = rpc_permission_verify(user_cached)
                if userrole_dd:
                    return run(self.oauth_rpc_host, data, arg)
                else:
                    error_str = "没有操作权限!"
                    return {'401': error_str}
            else:
                error_str = "用户没有登录!"
                return {'401': error_str}

        elif data.get('token'):
            user_cached = run(self.oauth_rpc_host, data, "user")
            if user_cached:
                userrole_dd = rpc_permission_verify(user_cached)
                if userrole_dd:
                    return run(self.oauth_rpc_host, data, arg)
                else:
                    error_str = "没有操作权限!"
                    return {'401': error_str}
            else:
                error_str = "用户没有登录!"
                return {'401': error_str}

    def authorization_verify(self, data, arg):
        return run(self.oauth_rpc_host, data, arg)

    def permission_verify(self, data, arg):
        return run(self.oauth_rpc_host, data, arg)

    def redis_verify(self, data, arg):
        return run(self.oauth_rpc_host, data, arg)

    def bind(self):
        def wrapper(func):
            if self.kafka_callback:
                raise AttributeError('有存在的topic')
            self.kafka_callback = func
        return wrapper
