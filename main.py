import typer
from modulos.sockets.server import Server
from client.app import AppClient


app = typer.Typer()


@app.command(name="server")
def servidor(address: str = '127.0.0.1', port: int = 12345):
    server = Server(address, port)
    try:
        server.run()
    except Exception as err:
        typer.Exit()
        raise err

# @app.command(name="client")
# def cliente(username: str, address: str = '127.0.0.1', port: int = 12345):
#     client = Client(address, port, username)
#     client.run()

@app.command(name="client")
def client():
    # run_client()
    app = AppClient()
    app.run()

if __name__ == "__main__":
    app()
