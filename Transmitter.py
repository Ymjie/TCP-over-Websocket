import asyncio
import functools
from time import sleep
import websockets
from Logger import Log
from functools import partial


class Transmitter:
    def __init__(self, listener, sender) -> None:
        # self.loop=asyncio.new_event_loop()
        self.listener = listener
        self.sender = sender
        self.start_listen()

    def start_listen(self):
        # 启动listen
        self.loop = asyncio.get_event_loop()
        crt = self.listener.creat_listen(self.handle, self.loop)
        try:
            server = self.loop.run_until_complete(crt)
            Log.debug(server)
            self.loop.run_forever()
        except Exception as e:
            Log.debug(e)

    async def handle(self, *obj):
        Log.debug('连接开始！')
        listener_recv = functools.partial(self.listener.recv, *obj)
        try:
            a = await self.sender.connect(self.loop)
            print(a)
        except Exception as e:
            Log.warning(e)
        # if not self.sender.websocket:
        # while not self.sender.websocket:
        #     sleep(0.1)
        #     a = self.sender.websocket
        sender_send = functools.partial(self.sender.send, *a)
        sender_recv = functools.partial(self.sender.recv, *a)
        listener_send = functools.partial(self.listener.send, *obj)
        task = [
            self.transTask(listener_recv, sender_send),
            self.transTask(sender_recv, listener_send)
        ]
        # try:
        await asyncio.gather(*task)
        # except Exception as e:
        #     Log.debug(e)
    @staticmethod
    async def transTask(mtd_recv, mtd_send):
        while True:
            # Log.debug('transTask:开始')
            try:
                data = await mtd_recv()
                await mtd_send(data)
            except Exception as e:
                Log.warning(e)
                break
