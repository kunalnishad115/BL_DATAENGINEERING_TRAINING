def is_valid(nums,mid,d):
  sum=0
  days=1
  for i in nums:
    sum+=i
    if sum>mid:
      days+=1
      sum=i
      if days>d:
        return False
      
  return True
  


def ship_valid(n,nums,days):
  left=max(nums)
  right=sum(nums)
  res=-1

  while left<=right:
    mid=left+(right-left)//2
    if is_valid(nums,mid,days):
      res=mid
      right=mid-1

    else:
      left=mid+1

  return res



n=int(input("length"))
days=int(input("enter the number of days:"))
nums=[]
for i in range(n):
  nums.append(int(input("enter the element")))

print(ship_valid(n,nums,days))