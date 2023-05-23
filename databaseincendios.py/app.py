
from fire import Fire
from firesdatabase import FireDatabase

database = FireDatabase()

def print_menu():
    print("""\n--- Menú ---
    1 - Guardar un incendio
    2 - Mostrar todos los incendios
    3 - Mostrar incendio por ID
    4 - Mostrar incendios por ciudad
    5 - Actualizar un incendio
    6 - Borrar un incendio por ID
    7 - Borrar todos los incendios
    8 - Salir de la aplicación\n""")

def create_fire():
    pass

def show_all_fires():
    pass

def show_fire_by_id():
    pass

def show_fires_by_city():
    pass

def update_fire():
    pass

def delete_fire_by_id():
    pass

def delete_all_fires():
    pass

if __name__ == '__main__':
    fire_db = FireDatabase()

    fire_db.insert_demo_data()

    while True:
        print_menu()
        option = input("Introduce una opción: ")

        if option == '1':
            create_fire()
        elif option == '2':
            show_all_fires()
        elif option == '3':
            show_fire_by_id()
        elif option == '4':
            show_fires_by_city()
        elif option == '5':
            update_fire()
        elif option == '6':
            delete_fire_by_id()
        elif option == '7':
            delete_all_fires()
        elif option == '8':
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")








   

