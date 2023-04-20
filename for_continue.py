''' 
Ejemplo de bucle for con palabra reservada continue qu salta a
la siguiente iteracion
'''


lechuga = [3.99, 'verduras']
tomates = [4.99, 'verduras']
escalopines = [12.99, 'carnes']
jack_daniels = [39.99, 'alcohol']
yogures = [4.50, 'lacteos']
queso = [14,99, 'lacteos']

productos = [lechuga, tomates, escalopines, jack_daniels, yogures, queso]

for producto in productos:
    # print(producto[0], producto[1])
    
    if producto[1] == 'alcohol':
        continue
    
    producto[0] *= 0.90
    
for producto in productos:
    
    print(producto)
        
        
        