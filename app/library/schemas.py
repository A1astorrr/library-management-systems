from pydantic import BaseModel, ConfigDict

class BookBase(BaseModel):
    title: str
    author: str
    year:  int
    
class BookCreate(BookBase):
    pass

class BookUpdate(BookCreate):
    pass

class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    status: str