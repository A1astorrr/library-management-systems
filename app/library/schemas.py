from pydantic import BaseModel, ConfigDict
import enum
from sqlalchemy import Enum

class Status(str, enum.Enum):
    available = "в наличии"
    issued = "выдана"
    
class BookBase(BaseModel):
    title: str
    author: str
    year:  int
    status: Status
    
class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    status: Status

class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    