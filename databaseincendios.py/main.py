
from fire import Fire
from firesdatabase import FireDatabase


fire_db = FireDatabase()



fire1 = Fire(id=None, street="calle Olvido", province="Madrid", level=4, data_from= (2022, 12, 11), data_to=(4, 2022, 1,1 ),active= " ",cause= "cortocircuito") 

fire2 = Fire(id=None, street="km.150 n-V", province="Toledo", level=2, data_from= (2022, 8, 15), data_to=(2022, 8, 17), active="True", cause="causas naturales") 

fire3 = Fire(id=None, street="Avenida Madrid",province="Cuenca", level=3, data_from=(2023, 1, 18), data_to=(2023, 1, 18), active=" ", cause="provocado")

fire4 = Fire(id=None, street="Avenida de la Paz", province="Guadalajara", level=1, data_from=(2023, 2, 1), data_to=(2023, 2, 1), active=" ", cause="por determinar")

fire5 = Fire(id=None, street="Km.35 n-II", province="Madrid", level=4, data_from=(2023, 3, 10), data_to=(2023, 3, 11), active="True", cause="por determinar")

fire_db.save(fire1)
fire_db.save(fire2)
fire_db.save(fire3)
fire_db.save(fire4)
fire_db.save(fire5)

