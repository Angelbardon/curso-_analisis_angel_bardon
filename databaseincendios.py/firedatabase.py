class FireDatabase:
    def __init__(self):
        self.database = []
        
    def find_all(self):
        return self.database.copy()
    
    def find_by_id(self, id):
        for fire in self.database:
            if fire.id == id:
                return fire 
        return None     
            
    def find_by_active(self, active):
        for fire in self.database:
            if fire.active == active:
                return fire
            
        return None    
        
    def find_by_cause(self, cause):
        for fire in self.database:
            if fire.cause == cause:
                return fire
            
        return None
            
            
    def find_all_by_fire(self, active, cause):
        filtered_fires = []
        
        for fire in self.database:
            if fire.active == active and fire.cause == cause:
                filtered_fires.append(fire)
        return filtered_fires
    
    def save(self, fire):
        
        id_maximo = 0
        for current_fire in self.travels:
            if current_fire.id > id_maximo:
                id_maximo = current_fire.id
                

        fire.id = id_maximo + 1
        
        self.fires.append(fire)
        
    def update(self, fire):
        for current_fire in self.database:
            if current_fire.id == fire.id:
                current_fire.street = fire.street
                current_fire.province = fire.province
                current_fire.level = fire.level
                current_fire.data_from = fire.data_from
                current_fire.data_to = fire.data_to
                current_fire.active = fire.active
                current_fire.cause = fire.cause
                return True
            
        return False
    
    def delete_by_id(self, id):
        for fire in self.fires:
            if fire.id == id:
                self.fires.remove(fire)
                break
            
    def delete_all(self):
        self.fires = []        
           
           
                   
                
                   
                 
                      
                     