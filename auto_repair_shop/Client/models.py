from pydantic import BaseModel

class ClientInput(BaseModel):
    first_name:str
    last_name:str
    password:int
    id_car:int

class ClientOutput(BaseModel):
    id:int
    first_name: str
    last_name: str
    password: int
    id_car: int
