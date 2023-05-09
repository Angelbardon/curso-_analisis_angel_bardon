
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
    
        





    
    
    
    
    
    
    
    
   