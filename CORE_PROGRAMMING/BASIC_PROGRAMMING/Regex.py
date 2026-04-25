import re as r
## search function in re modeule
data="pyrhon is good and good and good programming language"
pattern=r.compile(r"good|and",r.IGNORECASE) ## convert the regular expression object...

ans=r.search(pattern,data)
print(ans)
print(type(ans))


if ans:
  print("Found The Pattern: ", ans.group())
else:
  print("Not Found")


## r.finditr() in re

ans_itr=r.finditer(pattern,data)
print(ans_itr)
# for i in ans_itr:
#   print(i.group())
#   print(i.start())
#   print(i.end())


##  findall() in re 
 
ans_list=r.findall(pattern,data)
print(ans_list)





