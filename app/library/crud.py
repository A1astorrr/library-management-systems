from app.library.models import Book
from app.dao.base import BaseDAO
from app.database import async_session, Base
from sqlalchemy import select

class BookDAO(BaseDAO):
    model = Book
    
    @classmethod
    async def search(cls, title: str, author: str, year: int):
        async with async_session() as session:
            query = select(cls.model)
            if title:
                query =  query.filter(cls.model.title.ilike(f"%{title}%"))
            if author:
                query =  query.filter(cls.model.author.ilike(f"%{author}%"))
            if year:
                query =  query.filter(cls.model.year.ilike(f"%{year}%"))
            result  =  await session.execute(query)
            return result.scalars().all()