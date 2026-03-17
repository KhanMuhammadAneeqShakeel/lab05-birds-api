from fastapi import FastAPI
from database import start_db
from routers import species 
from routers import birdspotting
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


app = FastAPI()

@app.on_event("startup")
def on_startup():
    start_db()   


app = FastAPI()

@app.on_event("startup")
def on_startup():
    start_db()

app.include_router(species.router)


app.include_router(birdspotting.router)