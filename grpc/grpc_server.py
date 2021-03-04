from concurrent import futures
import time
import grpc

import translate_pb2 as translate_pb2
import translate_pb2_grpc as translate_pb2_grpc
from translate_main import main

class Translate(translate_pb2_grpc.TranslateServicer):
    def translate(self, request, context):
        file_data = main(request.job_id, request.file_name, request.file_data, request.src_lang, request.tgt_lang, request.eng)
        return file_data


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    translate_pb2_grpc.add_TranslateServicer_to_server(Translate(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server has started")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

# python grpc_server.py