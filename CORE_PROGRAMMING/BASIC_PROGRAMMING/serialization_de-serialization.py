import json as j
## serialize the list and dic into the json 
dummy_data=[
  {"name":"kunal","age":21,"city":"faridabad","domain":"data engineering"},
  {"name":"Rahul","age":21,"city":"Mathura","domain":"Java Developer"},
  {"name":"Aman","age":22,"city":"delhi","domain":"ui ux designer"},
  {"name":"Priya","age":26,"city":"kolkata","domain":"buisness analyst"},
  {"name":"Rohit","age":24,"city":"mumbai","domain":"data scientist"}
]

with open("data.json",'w') as f:
   j.dump(dummy_data,f,indent=4)


## de serialize the json data into list and dic


with open("data.json",'r') as f:
   data=j.load(f)
   print(type(data))
   print(data)