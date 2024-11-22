from typing import Sequence
from app.database import async_session, Base
from sqlalchemy import delete, select


class BaseDAO:
    model = Base

    @classmethod
    async def get_id(cls, book_id: int) -> Base | None:
        """Получает книги по ID."""
        async with async_session() as session:
            query = select(cls.model).filter_by(id=book_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **filter_by) -> Sequence[Base]:
        """Получает все книги с возможностью фильтрации."""
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_one_or_none(cls, **filter_by) -> Base | None:
        """Получает одну книгу или None по фильтру."""
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **data) -> Base:
        """Добавляет новую книги."""
        async with async_session() as session:
            added = cls.model(**data)
            session.add(added)
            await session.commit()
            return added

    @classmethod
    async def update(cls, book_id: int, **data) -> Base | None:
        """Обновляет книги по ID."""
        async with async_session() as session:
            updated = await cls.get_id(book_id)
            if updated is None:
                return None
            for key, value in data.items():
                setattr(updated, key, value)

            session.add(updated)
            await session.commit()
            return updated

    @classmethod
    async def delete(cls, **filter_by) -> Base | None:
        """Удаляет книги по фильтру."""
        async with async_session() as session:
            deleted = await cls.get_one_or_none(**filter_by)
            if deleted is None:
                return None
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
            return deleted
