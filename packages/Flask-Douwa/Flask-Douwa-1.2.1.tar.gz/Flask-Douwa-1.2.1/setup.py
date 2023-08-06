#coding:utf-8
from setuptools import setup


setup(
    name='Flask-Douwa',
    version='1.2.1',
    license='MIT',
    author='jhchen',
    author_email='watasihakamidesu@sina.cn',
    description=u'一个flask插件',
    long_description=__doc__,
    packages=['flask_douwa', 'flask_douwa.rpc', 'flask_douwa.protoparser', 'sequence_field', 'flask_douwa.rpc_client'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'grpcio==1.7.0',
        'protobuf==3.4.0',
        'ply==3.10',
        'msgpack-python==0.4.8',
        'confluent-kafka'

        #'kafka-python==1.3.6.dev0',
    ],
    classifiers=[
        'Framework :: Flask',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
