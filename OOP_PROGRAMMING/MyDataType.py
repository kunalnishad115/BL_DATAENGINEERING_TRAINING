class Fraction:
  def __init__(self,n,d):  #here n is numerator and d is denominator
    self.n=n
    self.d=d

  def __str__(self):
    return "{}/{}".format(self.n,self.d)
  
  def __add__(self,other):
    numerator_val= self.n * other.d + self.d * other.n
    denominator_val= self.d * other.d
    return "{}/{}".format(numerator_val,denominator_val)
  
  def __sub__(self,other):
    numerator_val= self.n * other.d - self.d * other.n
    denominator_val= self.d * other.d
    return "{}/{}".format(numerator_val,denominator_val)
  
  def __mul__(self,other):
    numerator_val=self.n * other.n
    denominator_val=self.d * other.d
    return "{}/{}".format(numerator_val,denominator_val)
  
  def __truediv__(self, other):
    numerator_val=self.n * other.d
    denominator_val=self.d * other.n
    return "{}/{}".format(numerator_val,denominator_val)
  

obj=Fraction(1,2)
obj2=Fraction(3,4)

print("The Value of obj is: ",obj)
print("The Value of obj2 is: ",obj2)

print(obj+obj2)
print(obj-obj2)
print(obj*obj2)
print(obj/obj2)

