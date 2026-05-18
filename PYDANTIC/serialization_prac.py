from pydantic import BaseModel


class Address(BaseModel):
    city: str


class Student(BaseModel):
    name: str
    address: Address


obj = Student(
    name="Kunal",
    address={"city": "Mathura"}
)


converted_obj=obj.model_dump()
json_converted_obj=obj.model_dump_json()
# print()

print(type(converted_obj))
print(type(json_converted_obj))