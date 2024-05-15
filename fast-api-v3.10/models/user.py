from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str

class Notes(BaseModel):
    id: str
    description: str