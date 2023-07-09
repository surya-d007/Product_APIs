from fastapi import FastAPI

app5 = FastAPI()


products = [
        {"name":"laptop","price":30000,"available_quantity":200},
        {"name":"computer","price":40000,"available_quantity":150},
        {"name":"earpods","price":7000,"available_quantity":300},
        {"name":"headphones","price":3000,"available_quantity":120},
        {"name":"type c chanrger","price":1250,"available_quantity":700},
        {"name":"mobile","price":20000,"available_quantity":1000},
        {"name":"ipod","price":60000,"available_quantity":190},
        {"name":"smartwatch","price":5000,"available_quantity":250},
        {"name":"Bluetooth speaker","price":2500,"available_quantity":400},
        {"name":"external hard drive","price":6000,"available_quantity":180},
        {"name":"printer","price":8000,"available_quantity":90},
        {"name":"wireless mouse","price":1000,"available_quantity":600},
        {"name":"keyboard","price":1500,"available_quantity":450},
        {"name":"portable SSD","price":7000,"available_quantity":350},
        {"name":"gaming console","price":25000,"available_quantity":80},
        {"name":"graphics card","price":15000,"available_quantity":200},
        {"name":"smartphone tripod","price":500,"available_quantity":800},
        {"name":"USB flash drive","price":500,"available_quantity":1000},
        {"name":"webcam","price":3000,"available_quantity":250},
        {"name":"Bluetooth earphones","price":2500,"available_quantity":500}
]
@app5.get("/update-product-quantity")
def update_quantity(product_name : str,New_quantity_to_be_added : int):
    for product in products:
        if product["name"] == product_name:
            product["available_quantity"] += New_quantity_to_be_added
            return product
    return {"error":"this product is a new product "}

@app5.get("/get-details/{product_name}")
def get_details(product_name : str):
    for product in products:
        if product["name"] == product_name:
            return product
    return {"error":"no such product available"}