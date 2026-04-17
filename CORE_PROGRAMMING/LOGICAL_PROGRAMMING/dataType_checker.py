
def my_decorator(data_type):
  def outer_wrapper(func):
    def inner_wrapper(*args):
      if type(args[0]) == data_type:
        print("valid data type")
        return func(*args)
      else:
        raise TypeError("invalid data type")
    return inner_wrapper
  return outer_wrapper

@my_decorator(int)
def square(num):
  print(num**2)
  
square(909)
