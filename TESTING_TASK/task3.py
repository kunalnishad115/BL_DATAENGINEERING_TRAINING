
class PatientValidationError(Exception):
  pass

def validate_patient(age,heart_rate):
  if age < 0 or age > 120:
    raise PatientValidationError("Invalid age Data")
  
  if heart_rate < 20 or heart_rate > 220:
    raise PatientValidationError("Invalid heart rate")
  
  return True
