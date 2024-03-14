# gRPC Python调用
通过一个简单的工作示例使用 Python 中的 gRPC。
1、定义rpc 接口 ,proto文件 hello.proto
2、安装对应的库，pip install  grpcio、pip install grpcio-tools、pip install grpc
3、生成py代码 
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. hello.proto
4、 得到两个文件hello_pb2.py 和 hello_pb2_grpc.py
5、 根目录定义server.py文件，作为启动服务端
6、 根目录定义client.py文件，作为客户端去连接服务端
