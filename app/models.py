from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

class Address(BaseModel):
    city: str
    country: str
    zip_code: str

class Item(BaseModel):
    product_id: int
    bought_quantity: int

class Order(BaseModel):
    id: Optional[str]
    timestamp: str
    items: List[Item]
    total_amount: float
    user_address: Address

