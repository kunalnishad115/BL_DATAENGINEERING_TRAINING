def pivot_index(n,my_list):
  total_sum=sum(my_list)
  left_sum=0
  for i in range(len(my_list)):
    right_sum=total_sum-left_sum-my_list[i]
    if left_sum==right_sum:
      print("Pivot Index is:",i)
      break
    left_sum+=my_list[i]

  return -1



n=(int(input("Enter the number of elements: ")))
my_list=[]
for i in range(n):
  my_list.append(int(input("Enter the element: "))) 

pivot_index(n,my_list)


  