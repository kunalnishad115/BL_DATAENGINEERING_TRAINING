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

