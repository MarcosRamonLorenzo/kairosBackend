from fastapi import APIRouter, HTTPException
from uuid import UUID


router = APIRouter()

fake_DB = {
    'hola': {'name': 'John Doe', 'age': 30}
}

@router.get('/me')
def getMe():
    return {"create":"user"}


@router.get('/{user_id}')
def getUser(user_id : str):
    
    print(f"Se ha solicitado el user_id: {user_id}") 

    if user_id not in fake_DB :
        raise HTTPException(status_code=404, detail="User not found ")
    return fake_DB[user_id]


@router.get('/users')
def getUsers():
    return {"create":"user"}





