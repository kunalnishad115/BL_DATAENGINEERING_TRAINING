import re
def is_valid(user_input):
  pattern=re.compile('[0-9#@$.]',re.IGNORECASE)
  ans=re.findall(pattern,user_input)
  if ans:
    print("Valid Pass")
  else:
    print("Invalid Pass")

user_input=input("Enter Your Pass: ")
is_valid(user_input)