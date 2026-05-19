from fastapi import FastAPI,status,HTTPException,Query
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
from fastapi.responses import JSONResponse
app=FastAPI()

##MOdel Creation

class Patient(BaseModel): ## Request Body....
  id:Annotated[str,Field(..., description='Id of The patient', examples=['P001'])]
  name:Annotated[str,Field(..., description='Name of the patient')]
  city:Annotated[str,Field(..., description='City of the patient')]
  age:Annotated[int , Field(..., gt=0,lt=150,description='Age of the Patient')]
  gender:Annotated[Literal['male','female','other'],Field(..., description='Gender Of the patient')]
  height:Annotated[float, Field(..., gt=0,description='Height of The patient')]
  weight:Annotated[float, Field(..., gt=0,description='weight of the patient')]


  @computed_field
  @property
  def bmi(self)-> float:
    formula=round(self.weight/(self.height**2),2)
    return formula
  
  @computed_field
  @property
  def verdict(self)-> str:
    if self.bmi < 18.5:
      return 'Underrate'
    elif self.bmi < 25:
      return 'Normal'
    elif self.bmi < 30:
      return 'Overweight'
    else:
      return 'Obese'
    

def load_data():
  with open('patients.json','r') as f:
    data=json.load(f)
  return data

def save_data(data):
  with open('patients.json','w') as f:
    json.dump(data,f)

@app.get('/',status_code=status.HTTP_200_OK)
def home_page():
  return {"msg":'home Page'}

@app.get('/view',status_code=status.HTTP_200_OK)
def get_data():
  data=load_data()
  return data

@app.get('/view/{id}',status_code=status.HTTP_200_OK)
def view_person(id:str):
  data=load_data()
  if id in data:
    return data[id]
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Patient Not Found')


@app.get('/sort')
def sort_vals(sort_by:str=Query(...,description='sort the values'),order:str=Query(default='asc',description='sort the values according to asc and desc')):
  valid_fields=['height','weight','bmi','age']
  if sort_by not in valid_fields:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='need a valid sort value')
  
  if order not in ['asc','desc']:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
  
  data=load_data()

  sort_order=True if order=='desc' else False

  sorted_data=sorted(data.values(),key=lambda x: x.get(sort_by,0),reverse=sort_order)

  return sorted_data


@app.post('/create')
def create_patient(p:Patient):
  ## load data
  data=load_data()
  ## validate it is unique
  if p.id in data:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='User Already Exist')
  ## if not then save User

  data[p.id]=p.model_dump(exclude=['id'])

  ## save into DB/Json

  save_data(data)
  return JSONResponse(status_code=status.HTTP_201_CREATED,content={'msg':'created...'})
  










