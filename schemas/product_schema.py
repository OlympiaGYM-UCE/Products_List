from pydantic import BaseModel

class ProductBase(BaseModel):
    nombre: str
    cantidad: int
    precio: float

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: str

    class Config:
        orm_mode = True