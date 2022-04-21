from __future__ import print_function

import asyncio
import logging
import random
from typing import Iterable, List

import grpc
import data_pb2
import data_pb2_grpc


async def stream_data(stub: data_pb2_grpc.DataStreamStub) -> None:
    data = stub.StreamData(data_pb2.DataRequest)
    async for point in data:
        print(point)

async def main() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = data_pb2_grpc.DataStreamStub(channel)
        print("-------------- Starting Data Stream --------------")
        await stream_data(stub)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())