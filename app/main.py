from fastapi import FastAPI
from app.config import Settings
from app.routers import items

settings = Settings()

app = FastAPI(
    title=settings.app_name,
    description="Учебный проект для демонстрации тестирования и деплоя",
    version="1.0.0",
    contact={
        "name": "Топакова Полина Васильевна",   
        "email": "topakovap04@mail.ru", 
    },
)

app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}