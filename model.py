from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base


class User(Base):
    __tablename__ = "Movie"
    name = Column(String(20))
    lastname = Column(String(40))
    age = Column(Integer)
    phone = Column(Integer, primary_key=True, index=True)
    adress = Column(Text())
    
