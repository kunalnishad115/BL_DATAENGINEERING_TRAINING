def peek_element(n,nums):
  if n==1:
    return 0
  if nums[0]>nums[1]:
    return 0
  if nums[n-1]>nums[n-2]:
    return n-1
  
  left=1
  right=n-2

  while left<=right:
    mid=left+(right-left)//2

    if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
      return mid
    elif nums[mid+1]>nums[mid]:
      left=mid+1
    else:
      right=mid-1

  return -1


n=int(input("length of the list"))
my_list=[]
for i in range(n):
  my_list.append(int(input("enter the element:")))

print(peek_element(n,my_list))