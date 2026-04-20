import json as j

class Student:
  def __init__(self, id,name , age , grade):
    self.id=id
    self.name=name
    self.age=age
    self.grade=grade

student=Student(3,"Kartik",22,'A')

def show_obj(student):
  if isinstance(student,Student):
    return {'id':student.id, 
            'name':student.name, 
            'age':student.age, 
            'grade':student.grade }
  

with open('test.json','r') as f:
  data=j.load(f)

data.append(student)

with open('test.json','w') as f:
  j.dump(data,f,default=show_obj,indent=4)
  






  
  






