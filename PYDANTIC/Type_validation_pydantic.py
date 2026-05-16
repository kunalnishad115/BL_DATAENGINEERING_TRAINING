from pydantic import BaseModel

class Type_Validator(BaseModel):
  name:str
  age:int
  issue:str

def appointed(vlt:Type_Validator):
  print(vlt.name)
  print(vlt.age)
  print(vlt.issue)
  print("Appointed Successfully")

def leave(vlt:Type_Validator):
  print(vlt.name)
  print(vlt.age)
  print("Patient Discharge")

data={
  'name':'ram',
  'age':34,
  'issue':'sick'
}
obj=Type_Validator(**data)
appointed(obj)
leave(obj)

