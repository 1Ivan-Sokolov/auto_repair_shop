from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,sessionmaker
from sqlalchemy import create_engine,ForeignKey

engine=create_engine('sqlite:///db.db')

class Base(DeclarativeBase):
    pass

class Application(Base):
    __tablename__='application'
    id:Mapped[int]=mapped_column(primary_key=True)
    date_of_addition:Mapped[datetime]
    id_car:Mapped[int]=mapped_column(ForeignKey('car.id'))
    id_malfunction:Mapped[int]=mapped_column(ForeignKey('malfuction.id'))
    errors_problems:Mapped[str]
    id_client:Mapped[int]=mapped_column(ForeignKey('client.id'))
    id_application_status:Mapped[int]=mapped_column(ForeignKey('application_status.id'))

class Client(Base):
    __tablename__='client'
    id:Mapped[int]=mapped_column(primary_key=True)
    first_name:Mapped[str]
    last_name:Mapped[str]
    password:Mapped[int]
    id_car:Mapped[int]=mapped_column(ForeignKey('car.id'))

class Car(Base):
    __tablename__='car'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    model:Mapped[str]


class Malfuction(Base):
    __tablename__='malfuction'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]

class Application_status(Base):
    __tablename__='application_status'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]

class Executor(Base):
    __tablename__ = 'executor'
    id:Mapped[int]=mapped_column(primary_key=True)
    first_name:Mapped[str]
    last_name:Mapped[str]

Base.metadata.create_all(engine)
Session=sessionmaker(engine,expire_on_commit=False)
