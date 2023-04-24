

prices = [10, 20, 30, 40, 50]

prices_iva = []

for price in prices:
    prices_iva.append(price * 1.21)
    
print(prices_iva)
    
 
 # Funcion lamda
  
prices = [10, 20, 30, 40, 50]

sumar_el_iva = lambda prices : prices * 1.21

resultado_total = list (map(sumar_el_iva, prices))

print (resultado_total)

# Funcion Def

def sumar_iv(price):
    return price * 1.21

print(f"El resultado es: {list(map(sumar_iva, prices))}")

# Funcion map con lamda

sumariva2 = lambda price: price * 1.21
print(f"El resultado con lambda es: {list(map(sumariva2, prices))}")