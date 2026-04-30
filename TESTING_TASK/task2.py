import re as r
def validate_employee(emp_id,email):
  emp_id_pattern=r"^EMP-\d{4}$"
  email_pattern=r"^[a-zA-Z0-9._%+-]+@company\.com$"

  if not r.match(emp_id_pattern,emp_id):
    raise ValueError("Invalid employee id")
  
  if not r.match(email_pattern,email):
    raise ValueError("Invalid Email")
  
  return True