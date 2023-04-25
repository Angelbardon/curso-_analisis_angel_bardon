# Asociacion
# Unidireccional solo desde un lado de la asociacion podemos acceder al objeto de la otra clase
# Por ejemplo: desde author puedo acceder a un libro, pero desde un libro no puedo acceder a ñun author


# Clase Book
class Book:
    def __init__(self, title, num_pages):
        self.title = title
        self.num_pages = num_pages

# Clase Author


class Author:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.books = []


book1 = Book('book1', 350)
book2 = Book('book2', 437)

author1 = Author('author', 2005)

author1.books = author1.books + [book1,book2]

print('fin')
#
