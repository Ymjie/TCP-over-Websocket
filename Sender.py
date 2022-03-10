import asyncio
import functools
from time import sleep
import websockets
from functools import partial


class Sender:
    pass


class TCP():
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port

    async def connect(self, loop):
        reader, writer = await asyncio.open_connection(self.ip, self.port)
        # print([reader, writer])
        return [reader, writer]

    @staticmethod
    async def send(reader, writer, data):
        if isinstance(data, str):
            data = data.encode()
        writer.write(data)
        await writer.drain()

    @staticmethod
    async def recv(reader, writer):
        data=  await reader.read(1024)
        if not data: 
            if not writer.is_closing():
                writer.close()
                await writer.wait_closed()
                raise Exception('TCP_Sender_关闭')
        return data


class Websocket:
    websocket = None

    def __init__(self, ip, port,) -> None:
        self.ip, self.port = ip, port

    async def connect(self, loop):
        return [await websockets.connect(f'ws://{self.ip}:{self.port}')]

    # async def wsconnect(self):
    #     print('尝试连接:'+f'ws://{self.ip}:{self.port}')
    #     async for websocket in websockets.connect(f'ws://{self.ip}:{self.port}'):
    #         try:
    #             self.websocket = websocket
    #             await websocket.wait_closed()
    #         except Exception as e:
    #             print(e)
    #             continue

    @staticmethod
    async def recv(websocket):
        return await websocket.recv()

    @staticmethod
    async def send(websocket, data):
        await websocket.send(data)
