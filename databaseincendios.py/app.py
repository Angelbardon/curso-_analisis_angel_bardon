
from fire import Fire
from firesdatabase import FireDatabase


def print_menu():
    print("""\n--- Menú ---
    1 - Guardar un incendio
    2 - Mostrar todos los incendios
    3 - Mostrar incendio por ID
    4 - Mostrar incendios activos
    5 - Mostrar incendios por causa
    6 - Mostrar incendios activos por causa
    7 - Actualizar un incendio
    8 - Borrar un incendio por ID
    9 - Borrar todos los incendios
    10 - Salir de la aplicación\n""")
    
def create_fire(fire_db):
    # Leer datos desde la consola
    street = input("Calle: ")
    province = input("Provincia: ")
    level = int(input("Nivel: "))
    date_from = input("Fecha de inicio (formato: AAAA-MM-DD): ")
    date_to = input("Fecha de fin (formato: AAAA-MM-DD): ")
    active = input("Activo (True/False): ")
    cause = input("Causa: ")
    
    fire = Fire(id=None, street=street, province=province, level=level, date_from=date_from, date_to=date_to, active=active, cause=cause)
    
    fire_db.save(fire)
    
    print("Incendio creado.")
    
def show_all_fires(fire_db):
    all_fires = fire_db.find_all()
    
    if all_fires:
        print("Lista de todos los incendios:")
        for fire in all_fires:
            print(f"ID: {fire.id}")
            print(f"Calle: {fire.street}")
            print(f"Provincia: {fire.province}")
            print(f"Nivel: {fire.level}")
            print(f"Fecha de inicio: {fire.date_from}")
            print(f"Fecha de fin: {fire.date_to}")
            print(f"Activo: {fire.active}")
            print(f"Causa: {fire.cause}")
            print("--------------------")   
    else:
        print("No se encontraron incendios en la base de datos.")
        
def show_fire_by_id(fire_db):
    fire_id = int(input("ID del incendio: "))
    fire = fire_db.find_by_id(fire_id)
    
    if fire:
        print("Detalles del incendio:")
        print(f"ID: {fire.id}")
        print(f"Calle: {fire.street}")
        print(f"Provincia: {fire.province}")
        print(f"Nivel: {fire.level}")
        print(f"Fecha de inicio: {fire.date_from}")
        print(f"Fecha de fin: {fire.date_to}")
        print(f"Activo: {fire.active}")
        print(f"Causa: {fire.cause}")
    else:
        print(f"No se encontró un incendio con ID {fire_id}.")

def show_active_fires(fire_db):
    active_fires = fire_db.find_by_active(True)
    
    if active_fires:
        print("Lista de incendios activos:")
        for fire in active   

