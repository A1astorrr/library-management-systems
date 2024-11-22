from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.config import settings

# Создание асинхронного движка базы данных
engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=False,
)

async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

class Base(DeclarativeBase):
    """Базовый класс для моделей SQLAlchemy."""
    pass
