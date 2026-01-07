from pydantic import BaseModel

# Pydantic documentation : https://docs.pydantic.dev/latest/

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int