class Vehicle:
    def __init__(self, name):
        self.name = name
class Car(Vehicle):
    def navigate(self):
        print(f'{self.name} bugatti')
class Truck(Vehicle):
    def navigate(self):
        print(f'{self.name} maruthi')
for v in [Car('john'),Truck('wick')]:
    v.navigate()