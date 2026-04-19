import collections

def isAnagram(s,t):
  s_counter=collections.Counter(s)
  t_counter=collections.Counter(t)
  return s_counter==t_counter


str_s=input("Enter the first string: ")
str_t=input("Enter the second string: ")
ans=isAnagram(str_s,str_t)
print(ans)