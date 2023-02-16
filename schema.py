from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    name = str
    lastname = str
    phone = int
    age = str
    adress = str
    

    class Config:
        orm_mode = True