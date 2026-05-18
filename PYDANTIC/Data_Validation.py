from pydantic import BaseModel,EmailStr,Field
from typing import List,Dict,Optional,Annotated

class Validator(BaseModel):
  name:Annotated[str,Field(title='Enter Your Name plz..',strict=True)]
  age:Optional[int]=Field(gt=0,lt=120)
  email:List[EmailStr]
  address:Dict[str,str]
  Hobby:Optional[str]=None

def profile(vlt:Validator):
  print("Hobby-Page-->")
  print("Name: ",vlt.name)
  print("Age: ",vlt.age)
  print("emails: ",vlt.email)
  print("address",vlt.address)
  print("Hobby: ",vlt.Hobby)

data={
  'name':'Karan',
  'age':56,
  'email':['k@gmail.com','a@gmail.com'],
  'address':{
    'pincode':'123456',
    'stree':'NH-14'
  },
  'Hobby':'BGMI'
}

obj=Validator(**data)
profile(obj)