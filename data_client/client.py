from __future__ import print_function

import asyncio
import logging

import redis
import os
import time

import grpc
import data_pb2
import data_pb2_grpc
from google.protobuf.json_format import MessageToDict

redis_conn = redis.StrictRedis(
    host=os.environ.get('REDIS_URL', 'localhost'),
    port=os.environ.get('REDIS_PORT', 6379),
    password=None,
    decode_responses=True
)

LAMBDA = float(os.environ.get('LAMBDA', 0.2))

async def stream_data(stub: data_pb2_grpc.DataStreamStub) -> None:
    data = stub.StreamData(data_pb2.DataRequest(lambda_arriv=LAMBDA))
    async for point in data:
        print(point)
        if not os.environ.get('SKIP_REDIS'):
            write_to_redis(point)

def write_to_redis(point: data_pb2.DataResponse):
    redis_conn.hset('service:time' , point.time, point.service)
    redis_conn.lpush("service:{}".format(LAMBDA), point.service)
    redis_conn.lpush('arrival:{}'.format(LAMBDA), point.interarrival)

async def main() -> None:
    async with grpc.aio.insecure_channel("{}:50051".format(os.environ.get('CLIENT_URL', 'localhost'))) as channel:
        stub = data_pb2_grpc.DataStreamStub(channel)
        print("-------------- Starting Data Stream --------------")
        await stream_data(stub)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())