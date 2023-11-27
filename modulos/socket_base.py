import socket

class MySocket:
    def __init__(self) -> None:
        self.socket = socket.socket(
            socket.AF_INET, # IPv4
            socket.SOCK_STREAM #TIPO (TCP)
        )
