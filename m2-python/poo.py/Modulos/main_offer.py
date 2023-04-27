
# importar de otro archivo siempre dentro de la misma carpeta

import offer

offer1 = offer.Joboffer(1, 'Programador Junior Python', 'ADECCO', 25000, 'remoto', 1)

# as permite asignar alias 

import offer as of

print(of.Joboffer.company)
