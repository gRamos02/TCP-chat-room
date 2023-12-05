# Python TCP CHAT Room
Cliente y Servidor para un chatroom simple en el cual los mensajes pasan por un middleware y ejemplifica la revision de errores de redundancia ciclica (CRC)

## Pasos para poder ejecutalos:


Primero crear el entorno virtual
```
python3 -m venv vevn
```

Activar el entorno virtual
```
venv/bin/activate
# o en windows
venv/Scripts/activate
```

Instalar dependencias 
```
pip install -r requirements.txt
```

Una vez instalado, se pueden ejecutar el servidor (actualmente limitado a 1 debido a que no se puede cambiar la direccion del host)

Para correr el servidor:
```
python3 server/
```

Para correr un cliente:
```
python3 client/
```
