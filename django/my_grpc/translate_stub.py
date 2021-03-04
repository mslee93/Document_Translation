import os
import grpc
from . import translate_pb2_grpc

TRANSLATE_HOSTNAME = '172.17.0.3' # 'mslee'
TRANSLATE_PORT = '50051'
TRANSLATE_CHANNEL = grpc.insecure_channel("{}:{}".format(TRANSLATE_HOSTNAME, TRANSLATE_PORT))
TRANSLATE_STUB = translate_pb2_grpc.TranslateStub(TRANSLATE_CHANNEL)