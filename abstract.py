from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass

class Dog(Animal):
    @property
    def species(self):
        return "john wick cananie"
dog = Dog()
print(dog.species)