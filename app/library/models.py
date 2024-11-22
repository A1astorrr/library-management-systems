from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True, index=True)]


class Book(Base):
    __tablename__ = "books"
    
    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(index=True)
    author: Mapped[str]
    year: Mapped[int]
    status: Mapped[str]