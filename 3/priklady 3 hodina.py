class Book:
  def __init__(self, title, pages, price):
    self.title = title
    self.pages = pages
    self.price = price


  def get_info(self):
    print (f"Kniha {self.title} s {self.pages} stranami stojí {self.price}")

  def discount(self, discountInPercent):
   self.price = self.price * (1 - discountInPercent/100)

book = Book("Maxipes Fík", "Kost", 500)
book.get_info()
book.discount(10)
book.get_info()


