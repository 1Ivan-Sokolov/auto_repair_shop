from pydantic import BaseModel

class ExecutorInput(BaseModel):
    first_name:str
    last_name:str

class ExecutorOutput(BaseModel):
    id:int
    first_name:str
    last_name:str
