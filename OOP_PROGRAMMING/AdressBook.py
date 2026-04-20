import json

class Person:
  def __init__(self,name, phone, email, city):
    self.name=name
    self.phone=phone
    self.email=email
    self.city=city

  def to_dict(self):
    return{
      'name':self.name,
      'phone':self.phone,
      'email':self.email,
      'city':self.city
    }
  
class AddressBook:
  def __init__(self):
    self.persons_list=[]

  def add_person(self,person):

    for p in self.persons_list:
      if p.name==person.name and p.phone==person.phone:
        print("Duplicate Not Allowed")
        return
      
    self.persons_list.append(person)
    print("Person Added Successfully")
      

  def del_person(self,person_name):
    for p in self.persons_list:
      if p.name.lower()==person_name.lower():
        self.persons_list.remove(p)
        return
      
    print("Person Not found...")


  def user_update(self,person_name):
    new_email=input("Enter Your New Email")
    new_city=input("Enter Your New City")

    for p in self.persons_list:
      if p.name.lower()==person_name.lower():
        p.email=new_email
        p.city=new_city
        return
      
    print("User Not Found...")

  def user_search(self,person_name):
    for p in self.persons_list:
      if p.name.lower()==person_name.lower():
        print(f"User Found He/Her From {p.city} city and its {p.email} email ")
        return
      

    print("User Not Found")


  def save_json(self):
    data=[]

    for p in self.persons_list:
      data.append(p.to_dict())

    with open('address.json','w') as f:
      json.dump(data,f,indent=4)

    print("Added...")

  def load_json(self):
    try:
      with open('address.json','r') as f:
        data=json.load(f)
    except:
      data=[]

    self.persons_list=[]

    for d in data:
      p=Person(d["name"],d["phone"],d["email"],d["city"])
      self.persons_list.append(p)
    

    print("Lodded...")

    

user=Person('Kanchan','782346782','k.Hyy@gmail.com','Mumbai')
obj = AddressBook()

obj.load_json()   

# obj.del_person("rohit")
obj.user_search('kunal nishad')


# obj.add_person(user)

obj.save_json()   







      
        
    


