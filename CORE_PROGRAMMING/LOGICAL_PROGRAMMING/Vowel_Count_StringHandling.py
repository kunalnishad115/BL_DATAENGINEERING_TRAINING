user_input=input("Enter a string:")
cnt=0

for ch in user_input:
  if ch in "aeiou":
    cnt+=1

print(cnt)