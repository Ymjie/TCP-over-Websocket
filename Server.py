from Transmitter import *
import Listener,Sender

if __name__=='__main__':
    TR = Transmitter(
    Listener.Websocket('127.0.0.1',5421),
    Sender.TCP('127.0.0.1',5201)
    )
    # ws://121.40.165.18:8800