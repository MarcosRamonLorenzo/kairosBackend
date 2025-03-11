from pydantic import BaseModel , EmailStr
from typing import Optional, List
from uuid import UUID


class UserBase(BaseModel):
    email : EmailStr
    
    
class UserCreate(UserBase):
    password : str
    
    
class UserResponse(UserBase):
    id: UUID


class EnterpriseUser(BaseModel):
    intitution_name : str
    phone : Optional[int] = None
    location : str
    images : List[str]
    schedule : List[str]
    
    
