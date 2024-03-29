# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import translate_pb2 as translate__pb2


class TranslateStub(object):
    """Service Definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.translate = channel.unary_unary(
                '/Translate.Translate/translate',
                request_serializer=translate__pb2.translateRequest.SerializeToString,
                response_deserializer=translate__pb2.translateResponse.FromString,
                )


class TranslateServicer(object):
    """Service Definition
    """

    def translate(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TranslateServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'translate': grpc.unary_unary_rpc_method_handler(
                    servicer.translate,
                    request_deserializer=translate__pb2.translateRequest.FromString,
                    response_serializer=translate__pb2.translateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Translate.Translate', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Translate(object):
    """Service Definition
    """

    @staticmethod
    def translate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Translate.Translate/translate',
            translate__pb2.translateRequest.SerializeToString,
            translate__pb2.translateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
