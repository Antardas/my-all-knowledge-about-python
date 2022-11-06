class Aircraft:

    def __init__(self, make, code, aircraftType, flight_range) -> None:
        self.make = make
        self.code = code
        self.aircraftType = aircraftType
        self.flight_range = flight_range

    def get_make(self):
        return self.make

    def __repr__(self) -> str:
        return f'Aircraft({self.make}, {self.code}, {self.aircraftType}, {self.flight_range})'
    
    