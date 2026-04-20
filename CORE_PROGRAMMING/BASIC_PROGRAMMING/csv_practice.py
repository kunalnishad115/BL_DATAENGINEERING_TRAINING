import csv 

dummy_data = [
  {"name":"kunal","age":21,"city":"faridabad","domain":"data engineering"},
  {"name":"Rahul","age":21,"city":"Mathura","domain":"Java Developer"},
  {"name":"Aman","age":22,"city":"delhi","domain":"ui ux designer"},
  {"name":"Priya","age":26,"city":"kolkata","domain":"buisness analyst"},
  {"name":"Rohit","age":24,"city":"mumbai","domain":"data scientist"}
]

with open('test.csv','w', newline="") as f:
    fieldnames = ["name","age","city","domain"]  
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(dummy_data)


