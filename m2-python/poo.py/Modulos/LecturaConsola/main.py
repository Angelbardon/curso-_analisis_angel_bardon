import datetime
# nombre = input('Introduzca su nombre\n')


# edad = int(input ('Introduce edad\n'))

# salary = float(input('Introduce salario\n'))

# apto = bool(int(input('0 Es NO apto, 1 SI es apto\n')))

# fecha_nacimiento_str =input('Introduce fecha nacimiento (YYYY-MM-DD) (1990-11-03\n)')
# fecha_nacimiento = datetime.date.fromisoformat(fecha_nacimiento_str)


fecha_nacimiento_str =input('Introduce fecha nacimiento (dd/MM/YYYY) (18/07/1999\n)')

fecha_array = fecha_nacimiento_str.split("/")

fecha_final = datetime.date(fecha_array[2], fecha_array[1], fecha_array[0])

print('fin')


