class Visitor:

    def __init__(self, name):
        self.name = name
        self.trips = []
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <= 15 and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception    




    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(self,new_trip, Trip):
            self.trips.append(new_trip)
            return self.trips
            
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        pass