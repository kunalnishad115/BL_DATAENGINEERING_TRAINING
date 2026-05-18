from pydantic import BaseModel


class Address(BaseModel):
    city: str
    pincode: int


class Student(BaseModel):
    name: str
    age: int
    address: Address


data = {
    "name": "Kunal",
    "age": 22,
    "address": {
        "city": "Mathura",
        "pincode": 281001
    }
}

obj = Student(**data)

print(obj)