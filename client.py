# -*- coding: utf-8 -*-
import grpc
# import stream_pb2
from proto import hello_pb2, hello_pb2_grpc


# import stream_pb2_grpc

# 启动客户端，与服务端进行连接，且发送请求
def run_client():
    # wit 上下文打开会自动关闭，

    # channel = grpc.insecure_channel('localhost:50051')  # 如果不写with 就是这样接收
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)  # 得到存根，存根就是代理，由这个代理去发送你的请求
        print("stub:", stub)  # 打印下存根，确保代理建立
        request = hello_pb2.HelloRequest(name='Tom')  # 定义要向服务端发送的内容
        # 这里同样要注意因为你proto里面定义的 请求的字段名就是name 所以必须用name='你要传的内容'的形式去包装请求，服务端才能识别

        response = stub.SayHello(request)  # 得到响应 与res = requests.get(url)一个意思
        print('Received response:', response.message)
        # 打印响应 也是同理，因为你proto里定义返回的字段名 所以必须用response.message去取这个值


if __name__ == '__main__':
    run_client()
    # # Get the returned data from the trailing metadata
