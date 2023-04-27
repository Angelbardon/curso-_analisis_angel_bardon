
class TravelDatabase:
    def __init__(self):
        self.travels = []

    def find_all(self):
        # return self.travels.copy()
        return list(self.travels)

    def find_by_id(self, id):
        for travel in self.travels:
            if travel.id == id:
                return travel
        
        return None 
    
    def find_all_by_city(self, city_from, city_to):
        filtered_travels = []
        
        for travel in self.travels:
            if travel.city_from == city_from and travel.city_to == city_to:  
                filtered_travels.append(travel)
                
        return filtered_travels
    
    def save(self, travel):
        
        id_maximo = 0
        for current_travel in self.travels:
            if current_travel.id > id_maximo:
                id_maximo = current_travel.id
                
        travel.id = id_maximo + 1
        
        self.travels.append(travel)
        
    def update(self, travel):
        
        current.city_from = travel.city_from
        current.price = travel.price
        
        for current.city_from in self.travels:
            if current.
        
        