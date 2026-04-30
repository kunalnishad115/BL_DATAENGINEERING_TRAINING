import re

class TransferError(Exception):
  pass


def transfer(from_account, to_account, amount, balance):
  account_no_pattern=r"^\d{10}$"

  if not re.match(account_no_pattern,from_account):
    raise TransferError("Invalid Account Number")
  
  if not re.match(account_no_pattern,to_account):
    raise TransferError("Invalid Account Number")
  
  if amount <= 0  :
    raise TransferError("Amount Must Be greater Than 0")
  if amount > balance :
    raise TransferError("Insufficient Funds")
  
  return True

