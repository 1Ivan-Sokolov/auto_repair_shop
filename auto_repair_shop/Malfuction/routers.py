from fastapi import APIRouter
from sqlalchemy import select
from base import Session
from base import Malfuction
from Malfuction.models import MalfuctionInput,MalfuctionOutput

router=APIRouter()

@router.post('/create_malfuction', response_model=MalfuctionOutput)
def create_malfuction(malfuction:MalfuctionInput):
    session=Session()
    new_malfuction=Malfuction(name=malfuction.name)
    session.add(new_malfuction)
    session.commit()
    session.close()
    return new_malfuction

@router.put('/update_malfuction/{id}', response_model=MalfuctionOutput)
def update_malfuction(id:int, update_malfuction:MalfuctionInput):
    session=Session()
    quere=select(Malfuction).where(Malfuction.id==id)
    malfuction=session.scalar(quere)
    malfuction.name=update_malfuction.name
    session.commit()
    session.close()
    return malfuction

@router.delete('delete_malfuction/{id}', response_model=MalfuctionOutput)
def delete_malfuction(id:int):
    session=Session()
    quere = select(Malfuction).where(Malfuction.id == id)
    malfuction = session.scalar(quere)
    session.delete(malfuction)
    session.commit()
    session.close()