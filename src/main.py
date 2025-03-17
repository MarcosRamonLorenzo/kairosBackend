from fastapi import FastAPI
from routes import router 
from exceptions import NotFoundException , not_found_exception_handler

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}


app.include_router(router, prefix="/api")


app.add_exception_handler(NotFoundException,not_found_exception_handler)

