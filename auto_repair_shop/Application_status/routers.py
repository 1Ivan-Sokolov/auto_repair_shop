from fastapi import APIRouter
from sqlalchemy import select
from base import Session
from base import Application_status
from Application_status.models import Application_statusOutput,Application_statusInput

router=APIRouter()

@router.post('/create_application_status', response_model=Application_statusOutput)
def create_application(applicationstatus:Application_statusInput):
    session=Session()
    new_application_status=Application_status(name=applicationstatus.name)
    session.add(new_application_status)
    session.commit()
    session.close()
    return new_application_status

@router.put('/update_application_status/{id}', response_model=Application_statusOutput)
def update_application_status(id:int, update_application_status:Application_statusInput):
    session=Session()
    quere=select(Application_status).where(Application_status.id==id)
    application_status=session.scalar(quere)
    application_status.name=update_application_status.name
    session.commit()
    session.close()
    return application_status

@router.delete('delete_application_status/{id}', response_model=Application_statusOutput)
def delete_application_status(id:int):
    session=Session()
    quere = select(Application_status).where(Application_status.id == id)
    application_status = session.scalar(quere)
    session.delete(application_status)
    session.commit()
    session.close()