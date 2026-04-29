import pytest as p

@p.fixture
def login_crendentials():
  return {
    "admin_username":"Kunal",
    "admin_Password":"1234"
  }

@p.fixture
def cook_food_test():
  print("Setup: Gas On and Vegies Cut")
  yield
  print("Teardown: Gas Off and utils are Cleaned")

@p.fixture(params=[90,99,23,156,26,87])
def validation_nums(request):
  return request.param
