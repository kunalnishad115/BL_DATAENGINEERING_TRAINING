user_input=input("Enter a string: ")

list_str=user_input.split()

freq={
}

for i in list_str:
  freq[i]=freq.get(i,0)+1

print(freq)


str_ans=""
for str in reversed(user_input):
  str_ans+=str

print(str_ans)
