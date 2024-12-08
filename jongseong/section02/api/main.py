from faker import Faker
from fastapi import FastAPI
import faker_commerce
from pydantic import BaseModel
from random import randint
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


class ResponseDTOItem(BaseModel):
    id: int
    name: str
    price: int


fake = Faker("ko-KR")
fake.add_provider(faker_commerce.Provider)


@app.get("/items/{item_id}", response_model=ResponseDTOItem)
def read_item(item_id: int):
    response = ResponseDTOItem(id=item_id, name=fake.ecommerce_name(), price=randint(1000, 10000))
    return response
