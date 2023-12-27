from pydantic import BaseModel

class CarInput(BaseModel):
    name:str
    model:str

class CarOutput(BaseModel):
    id:int
    name:str
    model:str

