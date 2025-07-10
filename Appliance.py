from abc import ABC,abstractmethod
class Appliance(ABC):
    @property
    @abstractmethod
    def turn_on(self):
        pass
class WashingMachine(Appliance):
    @property
    def turn_on(self):
        return 'Washing machine turned on'
class Fridge(Appliance):
    @property
    def turn_on(self):
        return 'Fridge turned on'
app=WashingMachine()
app1=Fridge()
print(app1.turn_on)
print(app.turn_on)

