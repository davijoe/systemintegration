import grpc

import echo_pb2
import echo_pb2_grpc


def run() -> None:
    user_text = input("Enter a message: ")

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = echo_pb2_grpc.EchoServiceStub(channel)
        response = stub.Echo(echo_pb2.Message(text=user_text))

    print("Server response:", response.text)


if __name__ == "__main__":
    run()
