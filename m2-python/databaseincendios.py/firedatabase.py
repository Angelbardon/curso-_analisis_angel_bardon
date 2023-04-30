class FireDatabase:
    def __init__(self):
        self.fires = []
        
    def find_all(self):
        return self.fires.copy()
    
    def find_by_id(self, id):
        for fire in self.fires:
            if fire.id == id:
                return fire  
            
    def find_by_active(self, active):
        for fire in self.fires:
            if fire.active == active:
                return True
            
        return None    
        
    def find_by_cause(self, cause):
        for fire in self.cause:
            if fire.cause == cause:
                return cause
            
            
    def find_all_by_fire(self, active, cause):
        filtered_fires = []
        
        for fire in self.fires:
            if fire.active == active and fire.cause == cause:
                filtered_fires.append(fire)
                
        return filtered_fires
    
                      
                     