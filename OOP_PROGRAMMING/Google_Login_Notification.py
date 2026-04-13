class SecuirityException(Exception):
  def __init__(self, msg):
    print(msg)

  def logout(self):
    print("Logout From All Logins")
    


class Login:
  def __init__(self,name,email,password,device):
    self.name=name
    self.email=email
    self.password=password
    self.device=device

  def login_notify(self,email,password,device):
    if self.device!=device:
      raise SecuirityException("New Login Detected! Please verify your identity.")
    if self.email==email and self.password==password:
      print(f"Welcome back, {self.name}!")
    else:
      raise SecuirityException("Invalid Credentials! Please try again.")


obj=Login("kunal","kunal@example.com","123","ios")
try:
    obj.login_notify("kunal@example.com","123","ios")
except SecuirityException as e:
    e.logout()
else:
    print("Login Successful!")
finally:
    print("Welcome user.")

