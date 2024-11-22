from fastapi import FastAPI
import uvicorn
from app.library.views import router as router_book
app = FastAPI()

app.include_router(router_book)

@app.get("/",
         tags=["Приветствие"])
def welcome() -> dict[str, str]:
    return {"message": "Welcome"}


if __name__  == "__main__":
    uvicorn.run("app.main:app", reload=True)