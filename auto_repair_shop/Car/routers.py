from fastapi import APIRouter
from sqlalchemy import select
from base import Session
from base import Car
from Car.models import CarInput, CarOutput

router=APIRouter()

@router.post('/create_car', response_model=CarOutput)
def create_car(car:CarInput):
    session=Session()
    new_car=Car(name=car.name, model=car.model)
    session.add(new_car)
    session.commit()
    session.close()
    return new_car

@router.put('/update_car/{id}', response_model=CarOutput)
def update_car(id:int, update_car:CarInput):
    session=Session()
    quere=select(Car).where(Car.id==id)
    car=session.scalar(quere)
    car.name=update_car.name
    session.commit()
    session.close()
    return car

@router.delete('delete_car/{id}', response_model=CarOutput)
def delete_car(id:int):
    session=Session()
    quere = select(Car).where(Car.id == id)
    car = session.scalar(quere)
    session.delete(car)
    session.commit()
    session.close()