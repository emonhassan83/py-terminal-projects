from abc import ABC

class Vehicle(ABC):
    speed = {
         'car': 50,
         'bike': 60
    }
    def __init__(self, vehicle_type, license_plate, rate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate


class Car(Vehicle):
    def __int__(self, vehicle_type, license_plate, rate):
        super.__init__(vehicle_type, license_plate, rate)


class Bike(Vehicle):
        def __int__(self, vehicle_type, license_plate, rate):
            super.__init__(vehicle_type, license_plate, rate)