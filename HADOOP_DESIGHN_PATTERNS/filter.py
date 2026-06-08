import sys

for line in sys.stdin:
    product_id,name,stock = line.strip().split(",")
    if int(stock) < 10:
        print(f"{name}\t{stock}")

