from fastapi import FastAPI
from controllers.product_controller import router as product_router
from mongoengine import connect

app = FastAPI()
app.include_router(product_router)

connect('name data base', host='mongodb://localhost:27017')