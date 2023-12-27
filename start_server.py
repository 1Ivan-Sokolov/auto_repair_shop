from fastapi import FastAPI
from Application.routers import router as application_router
from Application_status.routers import router as application_status_router
from Car.routers import router as car_router
from Executor.routers import router as executor_router
from Client.routers import router as client_router
from Malfuction.routers import router as malfuction_router
app=FastAPI()

app.include_router(router=application_router,prefix='/application')
app.include_router(router=application_status_router, prefix='/application_status')
app.include_router(router=car_router, prefix='/car')
app.include_router(router=executor_router,prefix='/executor')
app.include_router(router=client_router,prefix='/client')
app.include_router(router=malfuction_router,prefix='/malfuction')