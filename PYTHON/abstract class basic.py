from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def speed(self, vehicle_name, speed):
        pass

class FourWheeler(Vehicle):
    def speed(self, vehicle_name, speed):
        print(f"The {vehicle_name} is traveling at a speed of {speed} km/h.")

class TwoWheeler(Vehicle):
    def speed(self, vehicle_name, speed):
        print(f"The {vehicle_name} is traveling at a speed of {speed} km/h.")

# Create objects of the derived classes
four_wheeler = FourWheeler()
two_wheeler = TwoWheeler()

# Call the speed() method using the objects
four_wheeler.speed("Car", 120)
two_wheeler.speed("Motorcycle", 80)