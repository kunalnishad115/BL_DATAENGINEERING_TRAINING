## instance variable jo 

class Constructor:
  id=100000000
  # def __init__(self,name):
  #   self.name=name

  #   print("constructor called")


  # @staticmethod
  # def print_name():
  #   print(Constructor.id)
  #   print('static_method annotation')
  
  @classmethod
  def print_name1(cls):
    print(Constructor.id)
    print('class method annotation')

# obj=Constructor()
# obj.print_name()
Constructor.print_name1()
# print(Constructor.id)
# print(obj.id)
# print(obj.__dict__)

# class Student:
#   def m1(self):
#       self.a=11
#       self.b=21
#       self.c=34
#       print(self.a)
#       print(self.b)
#       print(self.c)

# s= Student()
# s.m1()
# print(s.__dict__)

## static variables jo class level pe hote hai 
    

