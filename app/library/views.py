from fastapi import APIRouter
from app.exceptions import BookDeleted, BookNotCreated, NotDeletedById, BookNotUpdate, BookUpdated
from app.library.crud import BookDAO
from app.library.schemas import BookBase, BookCreate, BookUpdate, Book

router = APIRouter(
    prefix="books",
    tags=["Книги"],
)

@router.post("/", response_model=Book)
async def create_book(book: BookCreate, status="в наличии"):
    created = await BookDAO.add(**book.model_dump())
    if created is None:
        raise BookNotCreated
    return created

@router.delete("/{book_id}/")
async def delete_book(book_id:  int):
    deleted = await BookDAO.delete(id=book_id)
    if deleted is None:
        raise NotDeletedById
    raise BookDeleted

@router.get("/search/", response_model=list[Book])
async def search_books(title: str, author: str, year: int):
    search = await BookDAO.search(title=title, author=author, year=year)
    return search

@router.get("/", response_model=list[Book])
async def get_books(skip: int = 0, limit:  int = 100):
    books = await BookDAO.get_all()
    return books[skip: skip + limit]


@router.put("/{book_id}/")
async def update_status_book(book_id: int, status: str):
    update_book = await BookDAO.update(book_id=book_id, status=status)
    if update_book is None:
        raise BookNotUpdate
    raise BookUpdated
    




