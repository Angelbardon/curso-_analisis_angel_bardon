# Modelo de datos
#MVC: Modelo Vista Controlaor
import datetime

# Clase usuario User: id, nif, brithday, email, phone, password

class User:
    
    # Metodo constructor
    def __init__(self, id, nif, brithday, email, phone, password):
        self.id = id
        self.nif = nif 
        self.brithday = brithday
        self.email = email
        self.phone = phone
        self.password = password
        
user1 = User(1, '52552551Z', datetime.date(1995, 1, 5), 'user1@gmail.com', '123212223', 'usuario1')
user2 = User(2, '22222551Y', datetime.date.fromisoformat("1975-01-25"), 'user2@gmail.com', '654226676', 'usuario2')
      
print(user1.brithday)
print(user2.brithday)