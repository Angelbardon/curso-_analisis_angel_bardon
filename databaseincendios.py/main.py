



from firedatabase import FireDatabase
firedatabase = FireDatabase

from fire import Fire

fire1 = Fire(id=None, street="calle Olvido", province="Madrid", level=4, data_from= (2022, 12, 11), data_to=(4, 2022, 1,1 ),active= " ",cause= "cortocircuito") 

fire2 = Fire(id=None, street="km.150 n-V", province="Toledo", level=2, data_from= (2022, 8, 15), data_to=(2022, 8, 17), active="True", cause="causas naturales") 

fire3 = Fire(id=None, street="Avenida Madrid",province="Cuenca", level=3, data_from=(2023, 1, 18), data_to=(2023, 1, 18), active=None, cause="provocado")

fire4 = Fire(id=None, street="Avenida de la Paz", province="Guadalajara", level=1, data_from=(2023, 2, 1), data_to=(2023, 2, 1), active=None, cause="por determinar")

fire5 = Fire(id=None, street="Km.35 n-II", province="Madrid", level=4, data_from=(2023, 3, 10), data_to=(2023, 3, 11), active=None, cause="por determinar")

firedatabase.save(fire1)
firedatabase.save(fire2)
firedatabase.save(fire3)
firedatabase.save(fire4)
firedatabase.save(fire5)


print("================= FIND ALL=================")
fire = firedatabase.find_all()
print(f"Longitud {len(fire1)}")
print(f"fire1; {Fire[0]}")
