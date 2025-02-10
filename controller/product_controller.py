from fastapi import APIRouter, HTTPException
from services.product_service import ProductService
from schemas.product_schema import ProductCreate, ProductResponse

router = APIRouter()
service = ProductService()

@router.get("/products", response_model=list[ProductResponse])
async def get_all_products():
    return service.get_all_products()

@router.post("/products", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    return service.create_product(product.dict())

# Similar para los demás endpoints (GET by ID, PUT, DELETE)