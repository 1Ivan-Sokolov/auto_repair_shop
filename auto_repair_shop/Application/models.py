from pydantic import BaseModel
from datetime import datetime

class ApplicationInput(BaseModel):
    date_of_addition: datetime
    id_car:int
    id_malfunction:int
    errors_problems:str
    id_client:int
    id_application_status:int

class ApplicationOutput(BaseModel):
    id:int
    date_of_addition: datetime
    id_car: int
    id_malfunction: int
    errors_problems: str
    id_client: int
    id_application_status:int