import grpc
from concurrent import futures
import kvstore_pb2
import kvstore_pb2_grpc

class KeyValueStoreServicer(kvstore_pb2_grpc.KeyValueStoreServicer):
    def __init__(self):
        self.store = {}

    def Get(self, request, context):
        value = self.store.get(request.key, "")
        return kvstore_pb2.GetResponse(value=value)

    def Put(self, request, context):
        self.store[request.key] = request.value
        return kvstore_pb2.PutResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kvstore_pb2_grpc.add_KeyValueStoreServicer_to_server(KeyValueStoreServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
