from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app4 = FastAPI()

class Item(BaseModel):
    productId: str
    boughtQuantity: int

class UserAddress(BaseModel):
    city: str
    country: str
    zipCode: str

class Order(BaseModel):
    orderID: str
    timestamp: datetime = None
    items: list[Item]
    totalAmount: float
    userAddress: UserAddress


orders = [
    Order(
        orderID="ORD12345",
        timestamp=datetime.now(),
        items=[Item(productId="P12345", boughtQuantity=1)],
        totalAmount=10.0,
        userAddress=UserAddress(city="New York", country="United States", zipCode="12345")
    ),
    Order(
        orderID="ORD23456",
        timestamp=datetime.now(),
        items=[Item(productId="P23456", boughtQuantity=2)],
        totalAmount=20.0,
        userAddress=UserAddress(city="London", country="United Kingdom", zipCode="12345")
    ),
    Order(
        orderID="ORD34567",
        timestamp=datetime.now(),
        items=[Item(productId="P34567", boughtQuantity=3)],
        totalAmount=30.0,
        userAddress=UserAddress(city="Paris", country="France", zipCode="12345")
    ),
    Order(
        orderID="ORD45678",
        timestamp=datetime.now(),
        items=[Item(productId="P45678", boughtQuantity=4)],
        totalAmount=40.0,
        userAddress=UserAddress(city="Tokyo", country="Japan", zipCode="12345")
    )
]

@app4.post("/create-orders")
def create_order(
    orderid: str,
    items: list[Item],
    totalAmount: float,
    city: str,
    country: str,
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

@app4.get("/get-orders-details/{order_id}")
def get_orders(order_id : str):
    for temp_order in orders:
        if temp_order.orderID == order_id:
            return temp_order

