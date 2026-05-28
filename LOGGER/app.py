from fastapi import FastAPI
import logging
from task_schema import Task_Logger
app=FastAPI()
logging.basicConfig(
  filename='log.txt',
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

dummy_data=[
  {'id':1,'status':0},
  {'id':2,'status':0},
  {'id':3,'status':0}
]

@app.get('/tasks')
def get_all_tasks():
  logger.info('Get The all Tasks Successfully')
  return dummy_data

# @app.get


