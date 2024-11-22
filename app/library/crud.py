from app.library.models import Book
from app.dao.base import BaseDAO
from app.database import async_session, Base
from sqlalchemy import select
from typing import Sequence

class BookDAO(BaseDAO):
    model = Book
    
    @classmethod
    async def search(cls, title: str|None = None, author: str|None = None, year: int|None = None) -> Sequence[Book]:
        """Ищет книги по заголовку, автору или году."""
        async with async_session() as session:
            query = select(cls.model)
            if title is not None:
                query = query.filter(cls.model.title.ilike(f"%{title}%"))
            if author is not None:
                query = query.filter(cls.model.author.ilike(f"%{author}%"))
            if year is not None:
                query = query.filter(cls.model.year == year)
            result  =  await session.execute(query)
            return result.scalars().all()