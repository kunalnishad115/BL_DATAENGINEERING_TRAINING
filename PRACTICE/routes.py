from fastapi import FastAPI
import requests

app=FastAPI()

DATA="https://jsonplaceholder.typicode.com/posts"

@app.get('/')
def home_page():
  return{
    'msg':'home-page'
  }


@app.get('/posts') ## get route
def get_all_data():
  response=requests.get(DATA)

  return{
    'data':response.json()
  }

@app.get('/posts/{id}')
def get_data_by_id(id: int):
  response=requests.get(f'{DATA}/{id}')
  return{
    'data':response.json()
  }

@app.post('/posts/save')
def post_data():
  new_post={
        "title": "FastAPI Learning",
        "body": "Learning CRUD Operations",
        "userId": 1
  }

  response=requests.post(DATA,json=new_post)

  return{
    'status-code':response.status_code,
    'data':response.json()
  }

@app.put('/posts/edit/{id}')
def update_data(id:int):
  updated_data={
        "id": id,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
  }

  response=requests.put(f'{DATA}/{id}',json=updated_data)
  return{
    'data':response.json()
  }

@app.delete('/posts/del/{id}')
def delete_data(id: int):
  response=requests.delete(f'{DATA}/{id}')
  return{
    'status_code':response.status_code,
    'data':'del okk'
  }

