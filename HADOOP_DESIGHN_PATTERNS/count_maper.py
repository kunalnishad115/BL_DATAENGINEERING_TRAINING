## maper code
import sys

for line in sys.stdin:
    cols = line.strip().split(",")
    region = cols[1]
    print(f"{region}\t1")

## reducer code 



current_key = None
count = 0
for line in sys.stdin:
    key,value = line.strip().split("\t")
    value = int(value)
    if current_key == key:
        count += value
    else:
        if current_key:
            print(current_key,count)
        current_key = key
        count = value

if current_key:
    print(current_key,count)


