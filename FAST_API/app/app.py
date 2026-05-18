from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def hello():
  return {'msg':'hello'}

@app.get('/buy/{id}')
def product(id:int):
  item=['mango','mongoose','haldi']
  return item[id]