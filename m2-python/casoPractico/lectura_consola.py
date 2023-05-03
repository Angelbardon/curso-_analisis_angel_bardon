
from input_reader import read_init, read_float
from travel import Travel
from travel_database import TravelDatabase

database = TravelDatabase()

while True:
    
    print(""" App de viajes
          1 - Consultaar viajes
          2 - Consultar un viaje por id
          3 - Consultar un viaje por ciudaad
          4 - Crear un nuevo viaje
          5 - Actualizar un viaje existene
          6 - Borrar un viaje por id
          7 - Borrar todos los viajes
          8 - Salir de la aplicacion \n
          """)
    option = int(input("Introduce una opcion\n"))
    if option == 1:
        for travel in database.find_all():
            print(travel)
    elif option == 2: 
        id = read_init("id")
        pass
    elif option == 3:
        pass
    elif option  == 4:
    # Leer datos de consola
    
        city_from = input("Introduce la ciudad origen")
        city_to = input("Introduce la ciudad de origen") 
        passengers = read_int("passengers")
        price = read_float("price") 
        #  Crear objeto travel con los datos de consola
        travel = Travel 
        pass
    elif option == 5:
        pass
    elif option == 6:
        pass
    elif option == 7:
        pass
    else option == 8:
        print("Hasta pronto")
        break