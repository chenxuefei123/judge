# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import onlinejudge_pb2 as onlinejudge__pb2


class OnlineJudgeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HealthCheck = channel.unary_unary(
        '/onlinejudge.OnlineJudge/HealthCheck',
        request_serializer=onlinejudge__pb2.HealthCheckRequest.SerializeToString,
        response_deserializer=onlinejudge__pb2.HealthCheckResponse.FromString,
        )
    self.JudgeCompiledTests = channel.unary_unary(
        '/onlinejudge.OnlineJudge/JudgeCompiledTests',
        request_serializer=onlinejudge__pb2.CompiledJudgeRequest.SerializeToString,
        response_deserializer=onlinejudge__pb2.CompiledJudgeResponse.FromString,
        )


class OnlineJudgeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def HealthCheck(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def JudgeCompiledTests(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OnlineJudgeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HealthCheck': grpc.unary_unary_rpc_method_handler(
          servicer.HealthCheck,
          request_deserializer=onlinejudge__pb2.HealthCheckRequest.FromString,
          response_serializer=onlinejudge__pb2.HealthCheckResponse.SerializeToString,
      ),
      'JudgeCompiledTests': grpc.unary_unary_rpc_method_handler(
          servicer.JudgeCompiledTests,
          request_deserializer=onlinejudge__pb2.CompiledJudgeRequest.FromString,
          response_serializer=onlinejudge__pb2.CompiledJudgeResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'onlinejudge.OnlineJudge', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))