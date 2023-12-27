from sqlalchemy import select
from base import Session
from base import Application
from Application.models import ApplicationOutput,ApplicationInput
from fastapi import APIRouter,Response

router = APIRouter()


@router.post('/create_application', response_model=ApplicationOutput)
def create_application(application:ApplicationInput):
    session=Session()
    new_application=Application(date_of_addition=application.date_of_addition,id_car=application.id_car,id_malfunction=application.id_malfunction,errors_problems=application.errors_problems,id_client=application.id_client,id_application_status=application.id_application_status)
    session.add(new_application)
    session.commit()
    session.close()
    return new_application

@router.put('/update_application/{id}', response_model=ApplicationOutput)
def update_application(id:int, update_application:ApplicationOutput):
    session=Session()
    quere=select(Application).where(Application.id==id)
    car=session.scalar(quere)
    car.date_of_addition=update_application.date_of_addition
    car.id_car=update_application.id_car
    car.id_application_status=update_application.id_application_status
    car.id_client=update_application.id_client
    car.id_malfunction=update_application.id_malfunction
    car.errors_problems=update_application.errors_problems
    session.commit()
    session.close()
    return car


@router.get('/{id}', response_model=ApplicationOutput)
def get_id(id:int):
    session=Session()
    quere=select(Application).where(Application.id==id)
    application=session.execute(quere).scalar()
    session.close()
    if not application:
        return Response('Таких заявок нет')
    return application


@router.delete('/delete_application', response_model=ApplicationOutput)
def delete_applecation(id:int):
    session=Session()
    quere=select(Application).where(Application.id==id)
    application=session.scalar(quere)
    session.delete(application)
    session.commit()
    session.close()