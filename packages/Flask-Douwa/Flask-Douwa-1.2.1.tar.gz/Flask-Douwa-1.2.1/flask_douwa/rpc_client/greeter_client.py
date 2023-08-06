# Copyright 2015 gRPC authors.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import json

import grpc

from . import rpc_data_pb2
from . import rpc_data_pb2_grpc
# import requests


def run(oauth_rpc_host, data, arg):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.


    # with grpc.insecure_channel('localhost:5000') as channel:
    channel = grpc.insecure_channel(oauth_rpc_host)
    stub = rpc_data_pb2_grpc.GreeterStub(channel)
    if isinstance(data, dict):
        data2 = json.dumps(data)
        _name = "+".join([data2, arg])
        # print(_name)
    if arg == "user" or arg == "user_list":
        response = stub.User(rpc_data_pb2.UserRequest(name=_name))
        # return json.loads(response.message)
        if response.message:
            return json.loads(response.message)
        else:
            return None

    elif arg == "group" or arg == "group_list":
        response = stub.Group(rpc_data_pb2.GroupRequest(name=_name))
        # return json.loads(response.message)
        if response.message:
            return json.loads(response.message)
        else:
            return None

    elif arg == "token" or arg == "authkey":
        response = stub.Authorization(rpc_data_pb2.AuthorizationRequest(name=_name))
        # print(response.message)
        if response.message:
            return json.loads(response.message)
        else:
            return None

    elif arg == "permission":
        response = stub.Permission(rpc_data_pb2.PermissionRequest(name=data))
        # return response.message
        if response.message:
            return response.message
        else:
            return None

    elif arg == "ttl" or arg == "expire":
        response = stub.Authorization(rpc_data_pb2.AuthorizationRequest(name=_name))
        # return json.loads(response.message)
        if response.message:
            return response.message
        else:
            return None

#
# if __name__ == '__main__':
#     run()
