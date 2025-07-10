class Pet:
    def __init__(self, name):
        self.name = name
class Cat(Pet):
    def make_sound(self):
        print(f'{self.name} sounds meowwwww!')
class Dog(Pet):
    def make_sound(self):
        print(f'{self.name} braks loud')
for v in [Cat('cat'),Dog('dog')]:
    v.make_sound()
