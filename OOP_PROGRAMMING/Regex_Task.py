import re
class Register:
  def __init__(self):
    # self.name=name
    self.email=""
    self.password=""

  def valid_email(self,email):
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email)
  
  def valid_password(self,password):
    pattern=r'^[a-zA-Z0-9#@]{6,}$'
    return re.match(pattern,password)

  def user_register(self):
    while True:

        email_new = input("Enter Your Valid Email: ")
        password_new = input("Enter Your Valid Password: ")

        if not self.valid_email(email_new):
            print("Need Valid Email")
            continue

        if not self.valid_password(password_new):
            print("Need The Valid Pass")
            continue

        self.email = email_new
        self.password = password_new

        print("User Register Successfully...")
        break

  def login_user(self):
    login_email=input("Enter Your Login Email: ")
    login_pass=input("Enter Your Login pass: ")

    if login_email==self.email and login_pass==self.password:
      print("Login Successfully")
    else:
      print("Invalid Credentials...")


obj=Register()
obj.user_register()
if obj.email and obj.password:
    obj.login_user()