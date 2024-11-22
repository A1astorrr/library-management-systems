from fastapi import APIRouter
from app.exceptions import BookNotCreated, NotDeletedById, BookNotUpdate, BookNotSearch
from app.library.crud import BookDAO
from app.library.schemas import BookCreate, Book, Status
from typing import Sequence

router = APIRouter(
    prefix="/books",
    tags=["Книги"],
)


@router.post("/", response_model=Book)
async def create_book(
    book: BookCreate,
) -> Book:
    """Создает новую книгу."""

    created = await BookDAO.add(**book.model_dump())
    if created is None:
        raise BookNotCreated
    return created


@router.delete("/{book_id}/")
async def delete_book(book_id: int) -> dict[str, str]:
    """Удаляет книгу по ID."""

    deleted = await BookDAO.delete(id=book_id)
    if deleted is None:
        raise NotDeletedById
    return {"detail": "Книга успешно удалена."}


@router.get("/search/", response_model=list[Book])
async def search_books(
    title: str | None = None, author: str | None = None, year: int | None = None
) -> Sequence[Book]:
    """Ищет книги по заданным параметрам."""

    if not title and not author and not year:
        raise BookNotSearch
    search = await BookDAO.search(title=title, author=author, year=year)
    return search


@router.get("/", response_model=list[Book])
async def get_books(skip: int = 0, limit: int = 100) -> Sequence[Book]:
    """Получает список всех книг с пагинацией."""
    
    books = await BookDAO.get_all()
    return books[skip : skip + limit]


@router.put("/{book_id}/")
async def update_status_book(book_id: int, status: Status) -> dict[str, str]:
    """Обновляет статус книги по ID."""
    
    update_book = await BookDAO.update(book_id=book_id, status=status)
    if update_book is None:
        raise BookNotUpdate
    return {"detail": "Статус книги успешно обновлен."}
