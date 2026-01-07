from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/")
def first_api_test():
    return "Test API"


# Dependency Injection 
def get_db():
    db = session()
    try:
        yield db 
    finally:
        db.close()

database_models.Base.metadata.create_all(bind=engine)

# Function if not call everytime
def init_db():
    db = session()
    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products: 
            db.add(database_models.Product(**product.model_dump()))

        db.commit()

init_db()

@app.get("/products")

def get_all_products(db: Session = Depends(get_db)):
    # Dependency injections
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_products.id == id:
        return db_products

    return "product not found"

@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product")
def update_product(id:int, product: Product, db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()

    if db_products: 
        db_products.name = product.name
        db_products.description = product.description
        db_products.price = product.price
        db_products.quantity = product.quantity
        db.commit()
        return "Updated products"
    else: 
        return "No Product Found"

@app.delete("/product")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()

    if db_products:
        db.delete(db_products)
        db.commit()
        return "Data successfully deleteds"
    else: 
        return "Product Not Found"