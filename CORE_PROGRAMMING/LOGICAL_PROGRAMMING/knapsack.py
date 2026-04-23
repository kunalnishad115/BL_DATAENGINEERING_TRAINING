## wt array
## val array
## weight/capacity 
def knapsack(wt,val,weight,n):
  if n==0 or weight==0:
    return 0
  if wt[n-1]<=weight:
    return max(
      val[n-1]+knapsack(wt,val,weight-wt[n-1],n-1),
      knapsack(wt,val,weight,n-1))
  else:
    return knapsack(wt,val,weight,n-1)


n=int(input("Enter the len of array: "))
val=[]
wt=[]
weight=int(input("Enter The capacity of Bag: "))

for i in range(n):
  val.append(int(input("Enter your Values: ")))
for i in range(n):
  wt.append(int(input("Enter The Values: ")))

print(knapsack(wt,val,weight,n))

