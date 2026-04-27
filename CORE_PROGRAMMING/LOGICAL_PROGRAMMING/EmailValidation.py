import re
def is_valid(user_input):
  pattern=re.compile('[@]',re.IGNORECASE)
  ans=re.findall(pattern,user_input)
  if ans:
    print("Valid email")
  else:
    print("Invalid email")



user_input=input("Enter Your email: ")
is_valid(user_input)