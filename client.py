import grpc
import kvstore_pb2
import kvstore_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = kvstore_pb2_grpc.KeyValueStoreStub(channel)

    # Put a key-value pair
    put_response = stub.Put(kvstore_pb2.PutRequest(key="name", value="Alice"))
    print(f"Put Success: {put_response.success}")

    # Get the value
    get_response = stub.Get(kvstore_pb2.GetRequest(key="name"))
    print(f"Get Response: {get_response.value}")

if __name__ == "__main__":
    run()
