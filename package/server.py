import socket
from socket_base import MySocket

class Server(MySocket):
    buffer_size = 1024

    def __init__(self, address: str, port: int) -> None:
        super().__init__()
        self.address = address
        self.port = port 
        self.socket.bind((address, port))
        self.socket.listen(1)
        

    def accept_connection(self):
        conn, addr = self.socket.accept()
        print(f"Cliente conectado desde: {addr}")
        conn.send(b'Bienvenio')
        return conn

    def __str__(self):
        return f"{self.address}:{self.port}"

if __name__ == '__main__':
    print("SERVIDOR TCP")
    server = Server('127.0.0.1', 12345)
    print(server.socket.getsockname())
    while True:
        print("Esperando conexion...")
        connection = server.accept_connection()

        while True:
            data = connection.recv(Server.buffer_size)
            data = data.decode('utf-8')
            print(f"Se recibio: {data}")

            if data.lower() == "quit":
                print(f"Cerrando conexion con {connection.getsockname()}...")
                connection.close()
                break
            
            msg = f"Eco {data}"
            connection.send(msg.encode('utf-8'))
    
    print('Cerrando...')
    server.close()
