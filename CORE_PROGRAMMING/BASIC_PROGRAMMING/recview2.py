
def decorator(func):
  def wrapper(*args):
    print("calculation")
    return func(*args)
  return wrapper

@decorator
def add(a,b):
  return a+b

@decorator
def sub(a,b):
  return a-b

@decorator
def avg(a,b):
  return (a+b)/2



print(add(2,3))
print(sub(2,3))
print(avg(2,3))


