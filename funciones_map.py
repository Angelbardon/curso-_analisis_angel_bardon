

prices = [10, 20, 30, 40, 50]

prices_iva = []

for price in prices:
    prices_iva.append(price * 1.21)
    
print(prices_iva)
    
 
 
  
prices = [10, 20, 30, 40, 50]

sumar_el_iva = lambda prices : prices * 1.21

resultado_total = list (map(sumar_el_iva, prices))

print (resultado_total)

