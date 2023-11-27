import typer
from modulos.server import Server

app = typer.Typer()


@app.command(name="server")
def servidor(address: str = '127.0.0.1', port: int = 12345):
    server = Server(address, port)
    try:
        server.run()
    except Exception as err:
        typer.Exit()
        raise err

@app.command(name="client")
def cliente(address: str = '127.0.0.1', port: int = 12345):
    print('Has abierto un cliente...')

if __name__ == "__main__":
    app()
