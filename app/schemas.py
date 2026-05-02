from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(
        ...,
        title="Название товара",
        description="Наименование товара, например 'Ноутбук'",
        example="Laptop",
    )
    price: float = Field(
        ...,
        title="Цена",
        description="Цена товара в долларах",
        ge=0.01,
        example=999.99,
    )

class Item(ItemCreate):
    id: int = Field(
        ...,
        title="ID товара",
        description="Уникальный идентификатор",
        example=1,
    )