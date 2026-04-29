import pytest as p
from task3 import validate_patient, PatientValidationError

## TASK 3 TEST CASES >>>>---------------------
def test_valid_details():

  ans=validate_patient(27,34)
  assert ans==True


def test_invalid_age():
  with p.raises(PatientValidationError, match="Invalid age Data"):
    validate_patient(2700,54)

def test_invalid_heart_rate():
  with p.raises(PatientValidationError,match="nvalid heart rate"):
    validate_patient(27,90000)
