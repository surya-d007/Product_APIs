from fastapi import FastAPI, Body
from pydantic import BaseModel
from datetime import datetime

app2 = FastAPI()

orders = []

class Item(BaseModel):
    productId: str
    boughtQuantity: int

class UserAddress(BaseModel):
    city: str
    country: str
    zipCode: str

class Order(BaseModel):
    orderID : str
    timestamp: datetime
    items: list[Item]
    totalAmount: float
    userAddress: UserAddress

@app2.post("/orders")
def create_order(
    orderid : str,
    items: list[Item] ,
    totalAmount: float ,
    city: str ,
    country: str ,
    zipCode: str 
):
    order = Order(
        orderID=orderid,
        timestamp=datetime.now(),
        items=items,
        totalAmount=totalAmount,
        userAddress=UserAddress(city=city, country=country, zipCode=zipCode)
    )

    orders.append(order)
    return {"message": "Order created successfully"}

@app2.get("/get-orders-details")
def get_orders(order_id : str):
    for temp_order in orders:
        if temp_order.orderID == order_id:
            return temp_order