class User_Details:
    def __init__(self, name, email, blog_name):
        self.name = name
        self.email = email
        self.blog_name = blog_name

    def display_user_details(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Blog Name: {self.blog_name}")

    def total_blogs_written(self):
        blog_List = []
        blog_List.append(self.blog_name)
        print(f"Total Blogs Written: {len(blog_List)}")

    def serch_blog(self, serchable_blog_name):
        if serchable_blog_name == self.blog_name:
            print(f"Blog '{serchable_blog_name}' found!")
        else:
            print(f"Oops... '{serchable_blog_name}' not found.")


class Personal_Blog:
    def __init__(self, content_type, content_duration):
        self.content_type = content_type
        self.content_duration = content_duration

    def display_blog_details(self):
        print(f"Content Type: {self.content_type}")
        print(f"Content Duration: {self.content_duration}")

    def edit_blog(self,new_content_type,new_content_duration):
        self.content_type=new_content_type
        self.content_duration=new_content_duration
        print("Blog details updated successfully!")
        self.display_blog_details()

    

user=User_Details("Kunal","123@gmail.com","Tech Blog")
user1=User_Details("Rahul","456@gmail.com","Travel Blog")
# user.display_user_details()
user.total_blogs_written()
user.serch_blog("Tech Blog")
user1.serch_blog("Tech Blog")



# blog=Personal_Blog("Tech Related"," 3 minutes"  )
# blog.display_blog_details()
# blog.edit_blog("Travel Related","5 minutes")


