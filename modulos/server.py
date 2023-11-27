# import socket
import threading
from .socket_base import MySocket


class Server(MySocket):
    BUFFER_SIZE = 1024
    connected_clients = []
    usernames = []

    #Constructor
    def __init__(self, address: str = '127.0.0.1', port: int = 12345) -> None:
        super().__init__()
        self.address = address
        self.port = port
        self.socket.bind((address, port))
        self.socket.listen(1)

    def __str__(self):
        return f"{self.address}:{self.port}"

    #Metodos privados
    def accept_connection(self):
        #Aceptar la conexion, regresar socket y direccion del cliente
        client, addr = self.socket.accept()
        #Guardar el usuario seleccionado en el cliente
        # Y tambien guardar el socket en sus respectivas listas
        username = client.recv(self.BUFFER_SIZE).decode()
        self.connected_clients.append(client)
        self.usernames.append(username)
        print(f"{username} conectado desde: {str(addr)}")
        client.send(f"Bienvenido, {username}".encode())
        self.send_message(f"{username} se ha unido...".encode(), client)
        return (client, addr)

    def disconnect_client(self, client):
        idx = self.connected_clients.index(client)
        username = self.usernames[idx]
        self.send_message(f"Server: {username} se desconecto...".encode, client)
        self.connected_clients.remove(client)
        self.usernames.remove(username)
        client.close()
        print(f"Se desconecto el usuario {username}")

    def send_message(self, message, __client):
        #Por cada cliente conectado se enviara el mensaje (ya codificado)
        for client in self.connected_clients:
            #A todos menos el emisot
            if client != __client:
                client.send(message)

    
    def process_messages(self, client):
        while True:
            try:
                msg = client.recv(self.BUFFER_SIZE)
                self.send_message(msg, client)
            except:
                self.disconnect_client(client)
                break


    #Metodos publicos
    def run(self):
        print(f"Servidor inicializado en {self}\nEsperando conexiones...")
        while True:
            try:
                client, addr = self.accept_connection()
                thread = threading.Thread(target=self.process_messages, args=(client,))
                thread.start()
            except KeyboardInterrupt:
                print("Se interrumpio el servidor")
                self.socket.close()



if __name__ == "__main__":
    print("SERVIDOR TCP")
    server = Server("127.0.0.1", 12345)
    print(server)
    while True:
        try:
            print("Esperando conexion...")
            connection, address = server.accept_connection()

            while True:
                data = connection.recv(Server.buffer_size)
                data = data.decode("utf-8")
                print(f"Se recibio: {data}")

                if data.lower() == "quit":
                    print(f"Cerrando conexion con {connection.getsockname()}...")
                    connection.close()
                    break

                msg = f"Eco {data}"
                connection.send(msg.encode("utf-8"))

            respuesta = input("¿Desea cerrar el servidor? (yes/no): ")
            if respuesta.lower() == "yes":
                break
        except KeyboardInterrupt:
            break

    print("\nCerrando...")
    server.socket.close()
