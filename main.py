from fastapi import FastAPI
from models import Product
app = FastAPI()
@app.get("/")
def greet():
    return {"message": "Welcome to Telusko  Trac"}


products = [
    Product(id=1, name="Product 1", description="Description 1", price=10.0, quantity=100),
    Product(id=2, name="Product 2", description="Description 2", price=20.0, quantity=200),
    Product(id=3, name="Product 3", description="Description 3", price=30.0, quantity=300),
    Product(id=4, name="Product 4", description="Description 4", price=40.0, quantity=400),
]
@app.get("/products")
def getProducts():
    return products

@app.get("/product/{product_id}")
def getProduct(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"message": "Product not found"}



@app.post("/product")
def addProduct(product: Product):
    products.append(product)
    return {"message": "Product added successfully", "product": product}

@app.put("/product/{product_id}")
def updateProduct(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return {"message": "Product updated successfully", "product": updated_product}
    return {"message": "Product not found"}


@app.delete("/product/{product_id}")
def deleteProduct(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted_product = products.pop(index)
            return {"message": "Product deleted successfully", "product": deleted_product}
    return {"message": "Product not found"}








