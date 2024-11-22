from fastapi import HTTPException, status

from fastapi import HTTPException, status


BookNotCreated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Ошибка в создание записи",
)

BookNotUpdate = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Запись не обновлена",
)

NotDeletedById = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Запись  не найден"
)


BookUpdated = HTTPException(
    status_code=status.HTTP_202_ACCEPTED, detail="Запись обновлена"
)

BookDeleted = HTTPException(status_code=status.HTTP_200_OK, detail="Запись удалена")
