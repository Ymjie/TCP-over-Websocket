from Transmitter import *
import Listener,Sender

if __name__=='__main__':
    TR = Transmitter(
    Listener.TCP('127.0.0.1',8888),
    Sender.Websocket('127.0.0.1',5678)
    )
    # ws://121.40.165.18:8800