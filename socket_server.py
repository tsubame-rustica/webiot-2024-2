import asyncio
import websockets

class SocketData:
    socket_protocol = None
    path = './data/get_action.txt'

    def __init__(self, port):
        self.port = port
        asyncio.run(SocketData.main(self))
        

    async def server_connect(websocket):
        SocketData.socket_protocol = websocket  # websocketをクラス内で使用できるようにする
        await SocketData.read_file()
        with open("./data/connect_id.txt", 'w', encoding='utf-8') as fl:
            fl.write(str(websocket))
            fl.close()
        async for message in websocket:
            with open(SocketData.path, 'w', encoding='utf-8') as f:
                f.write(str(message))
                f.close()

    async def send_msg(msg):
        print(msg)
        await SocketData.socket_protocol.send(msg)
        
    async def main(self):
        async with websockets.serve(SocketData.server_connect, "localhost", self.port):
            await asyncio.Future()  # run forever

    async def read_file():
        print("hello")
        while True:
            with open("./data/pos.txt", mode='r', encoding='utf-8') as f:
                msg = f.read()
                if (msg == ''):
                    continue
                elif (int(msg) > 0):
                    await SocketData.socket_protocol.send(msg)
            with open("./data/pos.txt", mode='w', encoding='utf-8') as fw:
                fw.write("")
        
            await asyncio.sleep(1)
cls = SocketData(8003)