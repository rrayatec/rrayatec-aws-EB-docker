from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar la lista de orígenes permitidos
# Asegúrate de incluir el origen de tu aplicación React aquí
origins = [
    "http://localhost:3000",  # Reemplaza con el origen de tu aplicación React
    "https://localhost:3000",
     "http://aws-front-prod.us-east-1.elasticbeanstalk.com",
      "https://aws-front-prod.us-east-1.elasticbeanstalk.com" # Si estás usando HTTPS
]

# Agregar CORSMiddleware a la aplicación FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Establece los orígenes permitidos
    allow_credentials=True,  # Permitir el envío de cookies
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Métodos HTTP permitidos
    allow_headers=["*"],  # Encabezados permitidos
)

@app.get("/")
async def read_root():
    return {"message": "Hello, from FastAPI!"}

# Iniciar la aplicación con uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)