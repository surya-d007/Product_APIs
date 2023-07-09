from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from fastapi_pagination import LimitOffsetPage, add_pagination, paginate
from datetime import datetime

app3 = FastAPI()
add_pagination(app3)

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
    items: List[Item]
    totalAmount: float
    userAddress: UserAddress

    class Config:
        arbitrary_types_allowed = True

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
    ),
    Order(
        orderID="ORD56789",
        timestamp=datetime.now(),
        items=[Item(productId="P56789", boughtQuantity=5)],
        totalAmount=50.0,
        userAddress=UserAddress(city="Sydney", country="Australia", zipCode="12345")
    ),
    Order(
        orderID="ORD67890",
        timestamp=datetime.now(),
        items=[Item(productId="P67890", boughtQuantity=6)],
        totalAmount=60.0,
        userAddress=UserAddress(city="Berlin", country="Germany", zipCode="12345")
    ),
    Order(
        orderID="ORD78901",
        timestamp=datetime.now(),
        items=[Item(productId="P78901", boughtQuantity=7)],
        totalAmount=70.0,
        userAddress=UserAddress(city="Toronto", country="Canada", zipCode="12345")
    ),
    Order(
        orderID="ORD89012",
        timestamp=datetime.now(),
        items=[Item(productId="P89012", boughtQuantity=8)],
        totalAmount=80.0,
        userAddress=UserAddress(city="Rome", country="Italy", zipCode="12345")
    ),
    Order(
        orderID="ORD90123",
        timestamp=datetime.now(),
        items=[Item(productId="P90123", boughtQuantity=9)],
        totalAmount=90.0,
        userAddress=UserAddress(city="Barcelona", country="Spain", zipCode="12345")
    ),
    Order(
        orderID="ORD01234",
        timestamp=datetime.now(),
        items=[Item(productId="P01234", boughtQuantity=10)],
        totalAmount=100.0,
        userAddress=UserAddress(city="New Delhi", country="India", zipCode="12345")
    ),
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
    ),
    Order(
        orderID="ORD56789",
        timestamp=datetime.now(),
        items=[Item(productId="P56789", boughtQuantity=5)],
        totalAmount=50.0,
        userAddress=UserAddress(city="Sydney", country="Australia", zipCode="12345")
    ),
    Order(
        orderID="ORD67890",
        timestamp=datetime.now(),
        items=[Item(productId="P67890", boughtQuantity=6)],
        totalAmount=60.0,
        userAddress=UserAddress(city="Berlin", country="Germany", zipCode="12345")
    )
]

@app3.post("/orders")
def create_order(
    orderid: str,
    items: List[Item],
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

@app3.get("/get-orders-details")
def get_orders(order_id: str):
    for temp_order in orders:
        if temp_order.orderID == order_id:
            return temp_order
@app3.get("/users")
def get_users() -> LimitOffsetPage[Order]:
    return paginate(orders)
