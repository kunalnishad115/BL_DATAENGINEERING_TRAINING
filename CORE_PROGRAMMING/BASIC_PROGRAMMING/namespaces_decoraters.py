## name Spaces example 

# from numpy import inner


a=5
def fun(): ## this is a localscope 
  a=10
  print(a)
fun()      ## this is a global scope
print(a)

## another example of name spaces

b=3
def fun1():
  global b
  b+=1
  print(b)
fun1()
print(b)

## another exmaples of name spaces

def outer(): ## this an enclosing scope
  def inner(): ## this is a local scope
    print("this is inner function")
  inner()
  print("this is outer function")

outer()
print("main function") ## this is a global scope

## another example of name spaces


def outer_1():
  x=100
  def inner_1():
    nonlocal x
    x+=1
    print(x)
  inner_1()

outer_1()
print("main function__")

## example of decorators

def decorator(func):
  def wrapper():
    print("####################")
    func()
    print("####################")

  return wrapper

def say_hello():
  print("Hello, World!")

decorated_say_hello = decorator(say_hello)
decorated_say_hello()

another_hello=decorator(say_hello)
another_hello()




