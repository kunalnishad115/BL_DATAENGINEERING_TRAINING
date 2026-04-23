
## single inheritance
class One:
  def m1(self):
    print("Parent class m1 method")
class Two(One):
  def m1(self):
    print("Child class m2 method")
c = One()
# c.m1()
c.m1()


## multilevel inheritance

class A:
  def m1(self):
    print("Parent class A: m1 Method")
class B(A):
  def m2(self):
    print("Child class B derived from A: m2 Method")
class C(B):
  def m3(self):
    print("Child class C derived from B: m3 Method")
obj=C()
obj.m1()
obj.m2()
obj.m3()


## multiple inheritance 

class P1:
  def m1(self):
    print("Parent1 Method")
class P2:
  def m2(self):
    print("Parent2 Method")
class C(P1, P2):
  def m3(self):
    print("Child Method")
c=C()
c.m1()
c.m2()
c.m3()



