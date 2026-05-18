from pydantic import BaseModel,field_validator,Field,EmailStr,model_validator
from typing import Annotated

class Validator(BaseModel):
  name:Annotated[str,Field(strict=True)]
  age:int
  email:str

  @model_validator(mode='after')
  def email_check(self):
    if '@' in self.email :
      return self.email
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



