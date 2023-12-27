from pydantic import BaseModel

class MalfuctionInput(BaseModel):
    name:str

class MalfuctionOutput(BaseModel):
    id:int
    name:str

