from fastapi import FastAPI
from app.config import Settings
from app.routers import items  

settings = Settings()
app = FastAPI(title=settings.app_name)

app.include_router(items.router)  

@app.get("/")
async def root():
    return {"message": "Hello, World!"}