'''
Estructura de control iterarivo o de repeticion

bucle for es ñuñna estructura determinada
'''

names =['juan', 'malala', 'rosa'] # estructura de datos siempre en plural

print('rosa' in names)

for name in names:
    print(name)
    
 # for numero in range   
for num in range(100):
    print(num)   
    
 # desde el 50 hasta 98 con paso 2
for num in range(50, 100, 2):
    print(num)  
    
 #  breack
print('Inicio del programa')
for numero in range(1, 11):
    if numero == 6:
        break  #rompe el bucle
    print(numero)
    
print('fin del programa')

# continue palabra reservada bucle for
name = ['Patricia', 'Jholman', 'Edu','Latifa', 'Alan', 'Rafa']

for name in names:
    if name == 'Alan':
        continue
    
    print('Hola' + name)

