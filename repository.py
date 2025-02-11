from sqlalchemy.orm import Session
from models import Producto

def get_productos(db: Session):
    return db.query(Producto).all()

