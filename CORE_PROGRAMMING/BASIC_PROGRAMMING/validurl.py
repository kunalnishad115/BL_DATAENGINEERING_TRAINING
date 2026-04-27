import re

urls_list = [
    "https://www.google.com",        # Valid
    "htp://google.com",             # Invalid
    "https://github.com/user/repo", # Valid
    "www.google.com",               # Invalid
    "ftp://files.server.com/file.txt", # Valid
    "https//missingcolon.com",      # Invalid
    "http://123.45.67.89",          # Valid
    "https://",                     # Invalid
    "https://my-site123.net",       # Valid
    "http:/oneslash.com"            # Invalid
]

pattern=re.compile("https?://\w+\.\w+")

for i in urls_list:
  if re.match(pattern,i):
    print("valid URL: ",i)
  else:
    print("Invalid URL: ",i)


mixed_data = [
    "Contact us at support@gmail.com or call 9876543210",
    "My email is john_doe123@yahoo.com for project updates",
    "Emergency helpline number is 9123456780 available 24/7",
    "Send your resume to careers@company.org",
    "Call me tomorrow at 8899776655 regarding the meeting",
    "Invalid email address: help@company",
    "Wrong phone number: 98AB567890",
    "Reach out at admin.site.com for details",
    "Office contact: office123@gmail.com and phone 9988776655",
    "Customer care number is 12345 and email support@domain.net"
]

pattern=r'\d+|\w+@\w+\.\w+'

for i in mixed_data:
  if re.search(pattern,i):
    print(f"Here is a Valid Data:{i}")
  else:
    print("Not found")

