from pydantic import BaseModel

class Application_statusInput(BaseModel):
    name:str

class Application_statusOutput(BaseModel):
    id:int
    name:str