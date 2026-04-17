import time


# def min_time_calci(t1,t2,t3):
#   print(f"The minimum execution time is: {min(t1,t2,t3)}")

# def max_time_calci(t1,t2,t3):
#   print(f"The maximum execution time is: {max(t1,t2,t3)}")

def time_calculator(func):
  def wrapper(*args):
    start_time=time.time()
    func(*args)
    end_time=time.time()
    print(f"Ececution time: {func.__name__} " ,end_time-start_time,"seconds")
  return wrapper

@time_calculator
def saying_hello():
  user_input=input("Enter your name: ")
  print(f"Hello, {user_input}!")


@time_calculator
def counting_numbers():
  count=0
  for i in range(10000000):
    count+=1
  print(f"Counted to {count}")


@time_calculator
def power_calculator():
  user_input=int(input("Enter Length "))
  my_List=[]
  for i in range(user_input):
    user_input=int(input("Enter the number: "))
    my_List.append(user_input)

  ans_list=[i**2 for i in my_List]
  print(ans_list)



t1=saying_hello()
t2=counting_numbers()
t3=power_calculator()




