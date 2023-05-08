


import datetime

from fire_database import FireDatabase
fire_database = FireDatabase()

from fire import Fire

fire1 = Fire(id=None, "calle Olvido", "Madrid", 4, datetime.date (2022, 12, 11), datetime.date (4, 2022, 1,1 ), " ", "cortocircuito") 

fire2 = Fire(id=None, "km.150 n-V", "Toledo", 2, datetime.date (2022, 8, 15), datetime.date(2022, 8, 17), "True", "causas naturales") 

fire3 = Fire(id=None, "Avenida Madrid", "Segovia", 3, datetime.date(2023, 1, 18), datetime.date(2023, 1, 18), None, "provocado")

fire4 = Fire(id=None, "Avenida de la Paz", "Leganes", 1, datetime.date(2023, 2, 1), datetime.date(2023, 2, 1), None, "por determinar")

fire5 = Fire(id=None, "calle luna", "Madrid", 4, datetime.date(2023, 2, 10), datetime.date(2023, 2, 10), None, "por determinar")



