from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.models import Product
from config.database import session, engine
from src import database_models
from sqlalchemy.orm import Session

app = FastAPI(
    title="Warungku - Test CICD",
    description="Playground with Fast-API Framework, and Devops CI/CD to develop simple warungku backend",
    version="V.3"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://warungku.projectsdev.site",
        "https://warungku.backend.projectsdev.site", 
        "http://localhost:8001", 
        "http://localhost:8000", 
        "http://localhost:3000", 
        "http://localhost:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def redirect_to_docs(): 
    return RedirectResponse(url="/docs")

products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10), 
    Product(id=2, name="laptop", description="gaming laptop", price=999, quantity=6),
    Product(id=3, name="camera", description="gaming laptop", price=999, quantity=6),
    Product(id=4, name="Accessoris", description="gaming laptop", price=999, quantity=6),
    Product(id=6, name="Powerbank", description="gaming laptop", price=999, quantity=6),
]

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

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_products.id == id:
        return db_products

    return "product not found"

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
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

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()

    if db_products:
        db.delete(db_products)
        db.commit()
        return "Data successfully deleteds"
    else: 
        return "Product Not Found"