

from fire import Fire
from firesdatabase import FireDatabase

def print_menu():
    print("""\n--- Menú ---
    1 - Mostrar todos los incendios
    2 - Buscar incendio por ID
    3 - Crear un nuevo incendio
    4 - Actualizar un incendio
    5 - Eliminar un incendio
    6 - Eliminar todos los incendios
    7 - Salir de la aplicación\n""")

def read_int(prompt):
    while True:
        try:
            value = int(input(prompt + ": "))
            return value
        except ValueError:
            print("Por favor, introduce un número entero válido.")

def read_float(prompt):
    while True:
        try:
            value = float(input(prompt + ": "))
            return value
        except ValueError:
            print("Por favor, introduce un número válido.")

def main():
    fire_db = FireDatabase()


    fire1 = Fire(id=None, street="calle Olvido", province="Madrid", level=4, date_from=(2022, 12, 11), date_to=(2022, 1, 1), active=" ", cause="cortocircuito")
    fire2 = Fire(id=None, street="km.150 n-V", province="Toledo", level=2, date_from=(2022, 8, 15), date_to=(2022, 8, 17), active="True", cause="causas naturales")
    fire3 = Fire(id=None, street="Avenida Madrid", province="Cuenca", level=3, date_from=(2023, 1, 18), date_to=(2023, 1, 18), active=" ", cause="provocado")
    fire4 = Fire(id=None, street="Avenida de la Paz", province="Guadalajara", level=1, date_from=(2023, 2, 1), date_to=(2023, 2, 1), active=" ", cause="por determinar")
    fire5 = Fire(id=None, street="Km.35 n-II", province="Madrid", level=4, date_from=(2023, 3, 10), date_to=(2023, 3, 11), active="True", cause="por determinar")
    
    fire_db.save(fire1)
    fire_db.save(fire2)
    fire_db.save(fire3)
    fire_db.save(fire4)
    fire_db.save(fire5)

    while True:
        print_menu()
        option = read_int("Introduce una opción")

        if option == 1:
            all_fires = fire_db.find_all()
            for fire in all_fires:
                print(fire)

        elif option == 2:
            fire_id = read_int("ID del incendio")
            fire = fire_db.find_by_id(fire_id)
            if fire:
                print(fire)
            else:
                print(f"No se encontró un incendio con ID {fire_id}.")

        elif option == 3:
            street = input("Calle: ")
            province = input("Provincia: ")
            level = read_int("Nivel")
            date_from = input("Fecha de inicio (formato: AAAA-MM-DD): ")
            date_to = input("Fecha de fin (formato: AAAA-MM-DD): ")
            active = input("Activo (True/False): ")
            cause = input("Causa: ")

            fire = Fire(id=None, street=street, province=province, level=level, date_from=date_from, date_to=date_to, active=active, cause=cause)
            fire_db.save(fire)

            print("Incendio creado correctamente.")

        elif option == 4:
            fire_id = read_int("ID del incendio a actualizar")
            fire = fire_db.find_by_id(fire_id)
            if fire:
                print("Ingrese los nuevos datos del incendio:")
                street = input("Calle: ")
                province = input("Provincia: ")
                level = int(input("Nivel: "))
                date_from = input("Fecha de inicio (formato: AAAA-MM-DD): ")
                date_to = input("Fecha de fin (formato: AAAA-MM-DD): ")
                active = input("Activo (True/False): ")
                cause = input("Causa: ")
        
                fire.street = street
                fire.province = province
                fire.level = level
                fire.date_from = date_from        
                fire.date_to = date_to
                fire.active = active
                fire.cause = cause

                print("Incendio actualizado correctamente.")        
            else:
                print(f"No se encontró un incendio con ID {fire_id}.")

        elif option == 5:
            fire_id = read_int("ID del incendio a eliminar")
            fire = fire_db.find_by_id(fire_id)
            if fire:
                fire_db.delete_by_id(fire_id)
                print("Incendio eliminado correctamente.")
            else:
                print(f"No se encontró un incendio con ID {fire_id}.")

        elif option == 6:
            fire_db.delete_all()
            print("Todos los incendios han sido eliminados.")

        elif option == 7:
            print("Hasta la próxima.")
            break

        



