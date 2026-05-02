from fastapi import APIRouter, HTTPException, Path, Query
from app.schemas import Item, ItemCreate

router = APIRouter(
    prefix="/items",
    tags=["items"],   
)

fake_db = {}
counter = 0

@router.post(
    "/",
    response_model=Item,
    summary="Создать новый товар",
    description="Добавляет товар в базу данных и возвращает его с присвоенным ID.",
    response_description="Созданный товар с полем id",
    responses={
        400: {"description": "Неверные данные товара"},
    },
)
async def create_item(item: ItemCreate):
    global counter
    counter += 1
    new_item = Item(id=counter, **item.model_dump())
    fake_db[counter] = new_item
    return new_item

@router.get(
    "/{item_id}",
    response_model=Item,
    summary="Получить товар по ID",
    description="Возвращает товар, если он существует.",
    response_description="Товар из БД",
)
async def get_item(
    item_id: int = Path(
        ...,
        title="ID товара",
        description="Уникальный идентификатор товара",
        ge=1,
        example=1,
    ),
    q: str | None = Query(
        None,
        title="Поисковый запрос",
        description="Дополнительный фильтр по названию",
    ),
):
    if item_id not in fake_db:
        raise HTTPException(404, detail="Item not found")
    return fake_db[item_id]