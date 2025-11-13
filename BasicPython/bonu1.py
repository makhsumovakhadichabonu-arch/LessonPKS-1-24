class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def info(self):
        print(f"{self.title} {self.author} {self.price}")

    def discount(self, percent):
        self.price -= self.price * percent / 100
        print(f"New price: {self.price} som")


v = Book("Yarry Potter", "ufhff", 2355)
v. info()                                                                            
v.discount(25)
v.info()