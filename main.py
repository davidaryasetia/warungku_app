from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Test API"

products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10), 
    Product(id=2, name="laptop", description="gaming laptop", price=999, quantity=6),
    Product(id=3, name="camera", description="gaming laptop", price=999, quantity=6),
    Product(id=4, name="Accessoris", description="gaming laptop", price=999, quantity=6),
    Product(id=6, name="Accessoris", description="gaming laptop", price=999, quantity=6),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

    return "product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id:int, product: Product):
    for i in range(len(products)): 
        if products[i].id == id:
            products[i] = product
            return "Product addedd successfull"
    
    return "No Product Found"

