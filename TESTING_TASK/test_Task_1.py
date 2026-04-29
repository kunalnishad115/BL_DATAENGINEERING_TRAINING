import pytest as p
from TESTING_TASK.task1 import calculate_total

## TASK 1 TEST CASES >>>>---------------------
def test_valid_price():
  items=[100,200]
  tax_rate=0.1

  ans=calculate_total(items,tax_rate)

  assert ans==330

def test_negative_price():
  with p.raises(ValueError, match="Negative Item Price is not acceptable"):

    calculate_total([100,-23],0.1)

def test_invalid_text_rate():
  with p.raises(ValueError,match="Enter The valid taxrate"):
    calculate_total([1000,1000],2)




