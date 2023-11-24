import socket
from ..sockets.socket import MySocket

class Client(MySocket):
    def __init__(self) -> None:
        super().__init__()
        


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 12345 
    buffer_size = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print ("Cliente TCP")
    print (f"Conectando con host: {host}:{port}")

    s.connect((host, port))                         # conectando con el servidor 
    print(s.recv(buffer_size))

    while True:
        mensaje = str(input("-> "))
        s.send(mensaje.encode('utf-8'))             # envio mensaje

        if mensaje.lower() == "quit":               # orden de desconexión
            print ("Cerrando...")
            s.close()                               # cerrando socket
            break

        data = s.recv(buffer_size)                  # recepción respuesta
        data = data.decode('utf-8')
        print(f"Recibido: {data}")
