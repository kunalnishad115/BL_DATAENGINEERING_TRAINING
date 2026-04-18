class Book_Exception(Exception):
  def __init__(self,msg):
    print(msg)

class BookManagment:
  
  def __init__(self,book_name):
    if book_name=="":
      raise Book_Exception("We need a Book Name")
    self.book_name=book_name

  def inventory(self):
    with open("books.txt",'a') as f:
      f.write(self.book_name+'\n')
      

  def display_books(self):
    cnt=0
    with open("books.txt",'r') as f:
      for book in f:
        cnt+=1
        print(book.strip())
    print("Total Books in Inventory:",cnt)

  def serch_book(self,name):
    if name=="":
      raise Book_Exception("We need a Book Name")
    
    with open("books.txt", 'r') as f:
     for book in f:
        if book.strip() == name:
            print("Book Found")
            return
    print("Book Not Found")


# obj_1=BookManagment("Maths")
# obj_1.inventory()
# obj_1.display_books()
# obj_1.serch_book("Maths")

# obj_2=BookManagment("Science")
# obj_2.inventory()
# obj_2.display_books()
# obj_2.serch_book("Science")










  


