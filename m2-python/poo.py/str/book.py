
class Author:
    def __init__(self, id, nif, email, year, city, num_books=0):
        self.id = id
        self.nif = nif
        self.email = email
        self.year = year
        self.city = city
        self.num_books = num_books

    def __str__(self):
        # Opcion 1
        # return f"Author con id = {self.id}" \
            # f"nif = {self.nif} " \
            # f"email = {self.email} " \
            # f"year = {self.year} " \
            #  f"city = {self.city} " \
            # f'num_books = {self.num_books}'
            
            # Opcion 2
        return 'Author %s' % (self.nif)
        
            # Opcion 3
        # return 'Author %s %s %s' % (self.id, self.nif, self.email)
            
author1 = Author(1, '23223223R', 'author1@email.com', 2000, 'Madrid')
print(author1)
