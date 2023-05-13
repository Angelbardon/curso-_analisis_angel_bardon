




    ("""-------- Menu --------
    1. Mostrar todos los incendios
    2. Buscar incendio por ID
    3. Buscar incendio por estado
    4. Buscar incendio por causa
    5. Buscar incendios por estado y causa
    6. Agregar nuevo incendio
    7. Salir)
""")
    
option = int(input("Seleccione una opcion\n"))
    
def create_fire_from_input():
    id = input("ID del incendio: ")
    street = input("Calle: ")
    province = input("Provincia: ")
    level = int(input("Nivel (entero): "))
    data_from = input("Fecha inicio (AAAAMMDD): ")
    data_to = input("Fecha fin (AAAAMMDD): ")
    active = input("Estado (True/False): ")
    cause = input("Causa: ")
    
    return Fire(id, street, province, level, data_from, data_to, active, cause)

while True:
    
   

    if option == "1":
        fires = fire_db.find_all()
        print("Incendios:")
        for fire in fires:
            print(fire.id, fire.street, fire.province)
    
    elif option == "2":
        fire_id = input("Ingrese el ID del incendio: ")
        fire = fire_db.find_by_id(fire_id)
        if fire:
            print("Incendio encontrado:")
            print(fire.id, fire.street, fire.province)
        else:
            print("No se encontró ningún incendio con ese ID.")
            
    elif option == "3":
        active = input("Ingrese el estado del incendio (True/False): ")
        fire = fire_db.find_by_active(active)
        if fire:
            print("Incendio encontrado:")
            print(fire.id, fire.street, fire.province)
        else:
            print("No se encontró ningún incendio con ese estado.")
            
    elif option == "4":
        cause = input("Ingrese la causa del incendio: ")
        fire = fire_db.find_by_cause(cause)
        if fire:
            print("Incendio encontrado:")
            print(fire.id, fire.street, fire.province)
        else:
            print("No se encontró ningún incendio con esa causa.")
             
    elif option == "5":
        active = input("Ingrese el estado del incendio (True/False): ")
        cause = input("Ingrese la causa del incendio: ")
        fires = fire_db.find_all_by_fire(active, cause)
        if fires:
            print("Incendios encontrados:")
            for fire in fires:
                print(fire.id, fire.street, fire.province)
        else:
            print("No se encontraron incendios con esos criterios.")
            
    elif option == "6":
        new_fire = create_fire_from_input()
        fire_db.save(new_fire)
        print("Incendio agregado")
        
    elif option == "7":
        print("Gracias por colaborar") 
        break          
                        
            