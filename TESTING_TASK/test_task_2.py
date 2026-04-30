import pytest as p
from task2 import validate_employee


## TASK 2 TEST CASES >>>>---------------------

def test_valid_emp():
  assert validate_employee("EMP-1234", "Kunal@company.com") == True

def test_invalid_emp_id():
  with p.raises(ValueError,match="Invalid employee id"):
    validate_employee("EMP-12","Kunal@company.com")

def test_invalid_emp_email():
  with p.raises(ValueError,match="Invalid Email"):
    validate_employee("EMP-1234","Kunal@gmail.com")