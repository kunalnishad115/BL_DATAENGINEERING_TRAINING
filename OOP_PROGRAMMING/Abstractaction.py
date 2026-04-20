from abc import ABC, abstractmethod

class Core_App(ABC): ## abstrcat class...
  def DB_Connnection(self):
    print("DB Connection Established")

  @abstractmethod
  def secuirity(self): ## abstract methods...
    pass


class Mobile_App(Core_App):
  def secuirity(self):
    print("Mobile App Security is Enabled")

  def Mobile_App_Feature(self):
    print("Mobile App Feature is Working")


class Web_App(Core_App):
  def secuirity(self):
    print("Web App Security is Enabled")

  def Web_App_Feature(self):
    print("Web App Feature is Working")



mobile=Mobile_App()
mobile.Mobile_App_Feature()
mobile.secuirity()

web=Web_App()
web.Web_App_Feature()
web.secuirity()

