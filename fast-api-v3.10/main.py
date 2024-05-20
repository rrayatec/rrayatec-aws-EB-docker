from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
import pymongo
import json
import os
# Modelos internos
import models.user as user

mongodb_key = os.getenv("MONGODB_KEY", 'mongodb://localhost:27017')
client = pymongo.MongoClient(mongodb_key) 
db = client["Escuela"] 
collection = db["alumno"] 
app = FastAPI(servers=[
            {"url": "/api/v1"},
            {"url": "http://hello-world.example/api/v1", "description": "Prod"},
    ],
    root_path="/api/v1",
    root_path_in_servers=False,)

# Configurar la lista de orígenes permitidos
origins = ["*"]

# Agregar CORSMiddleware a la aplicación FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Establece los orígenes permitidos
    allow_credentials=True,  # Permitir el envío de cookies
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Métodos HTTP permitidos
    allow_headers=["*"],  # Encabezados permitidos
)

@app.get("/getAllUsers", response_model=user.User)
def read_item():
    item = collection.find({})
    if item:
        json_str = json.dumps(list(item), indent=1, default=str)
        return Response(content=json_str, media_type='application/json')
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/findOneUser", response_model=user.User)
def read_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item:
        json_str = json.dumps(item, indent=1, default=str)
        return Response(content=json_str, media_type='application/json')
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/insertNewUser", response_model=user.User)
def create_item(item: user.User):
    result =  collection.insert_one(item.dict())
    item.id = str(result.inserted_id)
    return item

@app.put("/updateUser", response_model=user.User)
def update_item(item_id: str, item: user.User):
    updated_item = collection.find_one_and_update(
        {"_id": ObjectId(item_id)}, {"$set": item.dict()}
    )
    if updated_item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/deleteUser", response_model=user.User)
def delete_item(item_id: str):
    deleted_item = collection.find_one_and_delete({"_id": ObjectId(item_id)})
    if deleted_item:
        return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/")
async def read_root():
    return {"api => healthCheck": "OK...!"}

# Iniciar la aplicación con uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)