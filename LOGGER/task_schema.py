from pydantic import BaseModel,Field
from typing import Optional

class Task_Logger(BaseModel):
  id: int=Field(...,description='id of Task')
  status: bool=Field(...)

  