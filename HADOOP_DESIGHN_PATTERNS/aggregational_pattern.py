## mapper code 
import sys

for line in sys.stdin:
    supplier,cost = line.strip().split(",")
    print(f"{supplier}\t{cost}")

## reducer code 


current_supplier = None
total = 0
for line in sys.stdin:
    supplier,cost = line.strip().split("\t")
    cost = int(cost)
    if current_supplier == supplier:
        total += cost

    else:
        if current_supplier:
            print(current_supplier,total)
        current_supplier = supplier
        total = cost
if current_supplier:
    print(current_supplier,total)