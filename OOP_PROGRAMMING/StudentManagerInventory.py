import json
class Student:
  def __init__(self,id, name, marks,rollno):
    self.id=id
    self.name=name
    self.marks=marks
    self.rollno=rollno

  def to_dict(self):
    return{
      'id':self.id,
      'name':self.name,
      'marks':self.marks,
      'rollno':self.rollno
    }
  
class StudentManager:
  def __init__(self):
    self.students_list=[]

  def add_student(self,student):
    for s in self.students_list:
      if s.id==student.id and s.rollno==student.rollno:
        print("Duplicate Data Not Allowed")
        return
    
    self.students_list.append(student)

  def del_student(self,student_id):
    if type(student_id)!=int:
      print("need ont int value id")
      return 
    
    for s in self.students_list:
      if s.id==student_id:
        self.students_list.remove(s)
        return
      
    print("student not found...")

  def update_student(self,student_id):
    new_marks=int(input("Enter Your New Marks"))

    for s in self.students_list:
      if s.id==student_id:
        s.marks=new_marks
        return
      
    print("student not found...")

  def search_student(self,student_id):
    for s in self.students_list:
      if s.id==student_id:
        print(f""" 
        student found...
        name:{s.name},
        marks:{s.marks},
        rollno:{s.rollno}
""")   
      return 
    
    print("student not found...")

  def display_students(self):
    for s in self.students_list:
      print(f""" 
      name:{s.name},
      marks:{s.marks},
      rollno:{s.rollno}
""")
      
  def save_json(self):
    data=[]
    for s in self.students_list:
      data.append(s.to_dict())

    with open('sInventory.json','w') as f:
      json.dump(data,f,indent=4)

    print("Data Saved...")


  def load_json(self):
    try:
      with open('sInventory.json','r') as f:
        data=json.load(f)
    except:
      data=[]

    self.students_list=[]

    for d in data:
      s=Student(d["id"],d["name"],d["marks"],d["rollno"])
      self.students_list.append(s)

    print("Data Loaded...")


      
