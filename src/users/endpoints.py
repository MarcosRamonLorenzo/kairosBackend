from fastapi import APIRouter


router = APIRouter()

@router.get('/hola')
def createUser():
    return {"create":"user"}


