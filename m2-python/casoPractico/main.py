

"""
1.travel.py:
    
clase Travel
    id, city_from, city_to
    
2. traveldatabase.py:
clase TravelDatabase
    []
    def findAll
    def findById
    def findByCityFromAndCityTo 
    def insertçdef update
    def delete
3. app.py:
    pruebe todas las operaciones de TravelDatabase
    leer de input los datos para crear objetos Travel
    
Para entregar: Base de datos de incendios

1. fire.py
class Fire  
    id, street, province, level, date_from, date_to, active, cause
    
2. firedatabase.py
class FireDatabase
    []
    def findAll
    def findById
    def findByActiveTrue
    def findByCause(cause)
    def insert(fire)
    def update(fire)
    def delete(fire)
    
3. app.py
imprimir un menu que permita por consola ejecutar los metodos de FireData
leer de consola leer datos para crear incendios, filtrar, ect.
que el app inserte datos demo en el arranque
 
"""

 

# Crear 1 objeto TravelDatabase
from travel_database import TravelDatabase 
travel_database = TravelDatabase()

# Crear 5 objetos Travel utilizando el constructor
from travel import Travel
travel1 = Travel(id=None, city_from= 'Madrid', city_to= 'Barcelona', price=123.21, passengers=2)

# Crear los objetos Travel en TravelDatabase utilizando el constructor
travel_database.save(travel1)

# Probar metodos find
travels = travel_database.find_all()
print(f"Longitud {len(travels)}")
print(f"Viaje 1: {travels[0]}")
print(f"Viaje 2: {travels[1]}")

print("=============== FIND BY ID =============")


# Probar metodo update

# Probar delete y deleteall
print("==================== DELETE BY ID ===============")
