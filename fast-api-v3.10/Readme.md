## Dockerfile Fast-API

    Utiliza python:3.9-slim como la imagen base, que es una versión ligera de Python 3.9.

    Establece el directorio de trabajo en /app.

    Copia los archivos requirements.txt y main.py desde el sistema local al directorio de trabajo en la imagen.

    Instala las dependencias del archivo requirements.txt usando pip.

    Expone el puerto 8000 que la aplicación FastAPI usará para responder a las solicitudes HTTP.
    
    Especifica el comando para iniciar el servidor Uvicorn con tu aplicación FastAPI.