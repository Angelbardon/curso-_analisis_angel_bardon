import datetime
class Fire:
    def __init__(self, id, street, province, level, date_from, date_to, active, cause):
        self.id = id
        self.street = street
        self.province = province
        self.level = level
        self.date_from = date_from
        self.date_to = date_to
        self.active = active
        self.cause = cause
    def __str__(self):
        return f"{self.id} {self.street} {self.province} {self.level} {self.date_from} {self.date_to} {self.active} {self.cause}"
    
        
date_from = datetime.date.today()
date_to = datetime.date.today() 

fire1 = Fire("calle Olvido", "Madrid", 4, datetime.date (2022, 12, 11), datetime.date (4, 2022, 1,1 ), " ", "cortocircuito") 

fire2 = Fire("km.150 n-V", "Toledo", 2, datetime.date (2022, 8, 15), datetime.date(2022, 8, 17), "True", "causas naturales") 

fire3 = Fire("Avenida Madrid", "Segovia", 3, datetime.date(2023, 1, 18), datetime.date(2023, 1, 18), None, "provocado")

fire4 = Fire("Avenida de la Paz", "Leganes", 1, datetime.date(2023, 2, 1), datetime.date(2023, 2, 1), None, "por determinar")

fire3 = Fire("calle luna", "mMadrid", 4, datetime.date(2023, 2, 10), datetime.date(2023, 2, 10), None, "por determinar")


    
    
    
    
    
    
    
    
   