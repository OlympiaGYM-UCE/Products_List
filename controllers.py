from schemas import ProductoCreate
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config import SessionLocal, engine
from models import Base
import repository

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/productos/")
def listar_productos(db: Session = Depends(get_db)):
    return repository.get_productos(db)



