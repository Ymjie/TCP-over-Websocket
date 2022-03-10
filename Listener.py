import asyncio
import websockets


class Listener:
    pass


class TCP:
    def __init__(self, ip, port,) -> None:
        self.ip, self.port = ip, port

    def creat_listen(self, handle, loop):
        print(handle, loop)
        server = asyncio.start_server(handle, self.ip, self.port, loop=loop)
        return server

    @staticmethod
    async def recv(reader, writer):
        data=  await reader.read(1024)
        if not data: 
            if not writer.is_closing():
                writer.close()
                await writer.wait_closed()
                raise Exception('TCP_Listener_关闭')
        return data

    @staticmethod
    async def send(reader, writer, data):
        if isinstance(data, str):
            data = data.encode()
        writer.write(data)
        await writer.drain()


class Websocket:
    def __init__(self, ip, port,) -> None:
        self.ip, self.port = ip, port

    def creat_listen(self, handle, loop):

        start_server = websockets.serve(handle, self.ip, self.port)
        return start_server

    @staticmethod
    async def recv(websocket,path):
        return await websocket.recv()

    @staticmethod
    async def send(websocket,path, data):
        await websocket.send(data)
