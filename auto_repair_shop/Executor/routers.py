from fastapi import APIRouter, Response
from sqlalchemy import select
from base import Session
from base import Executor
from Executor.models import ExecutorOutput,ExecutorInput

router=APIRouter()

@router.get('/{id}', response_model=ExecutorOutput)
def get_id(id:int):
    session=Session()
    quere=select(Executor).where(Executor.id==id)
    executor=session.execute(quere).scalar()
    session.close()
    if not executor:
        return Response('Такого пользователя нет')
    return executor

@router.post('/create_executor', response_model=ExecutorOutput)
def create_executor(executor:ExecutorInput):
    session=Session()
    new_executor=Executor(first_name=executor.first_name,last_name=executor.last_name )
    session.add(new_executor)
    session.commit()
    session.close()
    return new_executor

@router.put('/update_executor/{id}', response_model=ExecutorOutput)
def update_executor(id:int, update_executor:ExecutorInput):
    session=Session()
    quere=select(Executor).where(Executor.id==id)
    executor=session.scalar(quere)
    executor.last_name=update_executor.last_name
    executor.first_name=update_executor.first_name
    session.commit()
    session.close()
    return executor

@router.delete('delete_executor/{id}', response_model=ExecutorOutput)
def delete_executor(id:int):
    session=Session()
    quere = select(Executor).where(Executor.id == id)
    executor = session.scalar(quere)
    session.delete(executor)
    session.commit()
    session.close()