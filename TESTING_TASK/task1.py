## TASK 1 --- E-commerce
def calculate_total(items,tax_rate):
  if tax_rate < 0 or tax_rate > 1:
    raise ValueError("Enter The valid taxrate")
  
  for item in items:
    if item < 0 :
      raise ValueError("Negative Item Price is not acceptable")
    
  sub_total=sum(items)

  total=sub_total+(sub_total*tax_rate)

  return total

