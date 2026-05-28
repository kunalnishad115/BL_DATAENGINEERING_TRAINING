from pydantic import BaseModel,field_validator,Field,EmailStr
from typing import Annotated

class Validator(BaseModel):
  name:Annotated[str,Field(strict=True)]
  age:Annotated[int,Field(gt=0,lt=110,strict=True)]
  email:Annotated[str,EmailStr]

  @field_validator('email')
  @classmethod
  def email_check(cls,val):
    if '@' in val:
      return val
    else:
      raise ValueError('check Your Email')
    
  
def print_dash(vlt:Validator):
  print(vlt.name)
  print(vlt.email)
  print(vlt.age)



data={
  'name':'kunal',
  'age':100,
  'email':'k@gmail.com'
}

obj=Validator(**data)
print_dash(obj)



