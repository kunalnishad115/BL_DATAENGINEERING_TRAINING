import pytest as p
from task4 import transfer, TransferError


## TASK 4 TEST CASES >>>>---------------------

def test_valid_transaction():
  assert transfer("1234567890","1234567890",500,10000)==True

def test_zero_amount():
  with p.raises(TransferError,match="Amount Must Be greater Than 0"):
    transfer("1234567890","1234567890",0,10000)

def test_insufficient_balance():
  with p.raises(TransferError , match="Insufficient Funds"):
    transfer("1234567890","1234567890",100,0)

def test_invalid_account_number():
  with p.raises(TransferError,match="Invalid Account Number"):
    transfer("1234567809909","1234567890",100,1000000)