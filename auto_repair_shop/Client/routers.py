from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from sqlalchemy import select
from base import Session
from base import Client
from Client.models import ClientInput,ClientOutput

router=APIRouter()

@router.get('/{id}', response_model=ClientOutput)
def get_id(id:int):
    session=Session()
    quere=select(Client).where(Client.id==id) # '''SELECT * FROM client WHERE client.id=id'''
    client=session.execute(quere).scalar()
    session.close()
    if not client:
        return Response('Такого пользователя нет')
    return client

@router.post('/create_client', response_model=ClientOutput)
def create_client(client:ClientInput):
    session=Session()
    new_client=Client(first_name=client.first_name,last_name=client.last_name,password=client.password,id_car=client.id_car )
    session.add(new_client)
    session.commit()
    session.close()
    return new_client

@router.post('/login', response_model=ClientOutput)
def login(login:ClientInput):
    session=Session()
    login=select(Client).where(Client.first_name==login.first_name,Client.password==login.password)
    client=session.scalar(login)
    session.close()
    if not client:
        return JSONResponse(status_code=404, content='Такого пользователя нет')
    return client

@router.put('/update_client/{id}', response_model=ClientOutput)
def update_client(id:int, update_client:ClientInput):
    session=Session()
    quere=select(Client).where(Client.id==id)
    client=session.scalar(quere)
    client.last_name=update_client.last_name
    client.first_name=update_client.first_name
    client.password=update_client.password
    client.id_car=update_client.id_car
    session.commit()
    session.close()
    return client

@router.delete('delete_executor/{id}', response_model=ClientOutput)
def delete_executor(id:int):
    session=Session()
    quere = select(Client).where(Client.id == id)
    executor = session.scalar(quere)
    session.delete(executor)
    session.commit()
    session.close()