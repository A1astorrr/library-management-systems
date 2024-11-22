from fastapi import HTTPException, status
from fastapi import HTTPException, status


BookNotCreated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Ошибка в создание книги.",
)

BookNotUpdate = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Книга не найдена.",
)

BookNotSearch = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Необходимо указать хотя бы один параметр поиска.",
)

NotDeletedById = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Книга не найдена."
)
