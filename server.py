# -*- coding: utf-8 -*-
import grpc
from concurrent import futures
# import proto.stream_pb2 as stream_pb2
# import proto.stream_pb2_grpc as stream_pb2_grpc

from proto import hello_pb2, hello_pb2_grpc
import time
import base64


# 继承 hello_pb2_grpc里面的 GreeterServicer 创建服务类，必须实现GreeterServicer里面的方法
class MyGreeterServicer(hello_pb2_grpc.GreeterServicer):
    # 定义服务，这个服务接收请求，返回响应
    def SayHello(self, request, context):
        # 在这里处理客户端的请求，并生成相应的响应数据
        print(request)  # request是请求，
        # 请求进来后这里可以写逻辑去处理请求，比如说判断计算之类的
        response_str = f"Hello, {request.name}"  # 把请求处理一下，等下返回出去，
        # 这里的request.name是因为你proto里定义的就是这个，发过来的 request是HelloRequest类型，
        # 内容是name:"输入的内容"，所以你要用request.name去拿到这个请求传入的内容

        response = hello_pb2.HelloReply(message=f"response: {response_str}")  # 定义响应，返回出去
        return response


# 启动服务
def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  # 设置服务线程，
    hello_pb2_grpc.add_GreeterServicer_to_server(MyGreeterServicer(), server)  # 服务添加进去
    server.add_insecure_port('[::]:50051')  # 定义服务端口
    server.start()  # 开启服务
    print("started server")  # 打印一下确定服务开启了
    server.wait_for_termination()  # 等待终止，就是关闭


if __name__ == '__main__':
    run_server()
