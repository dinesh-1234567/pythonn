class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def fun(self):
        print(f'{self.name} costs {self.price} rupee.')
person=Product('banana',20)
person.fun()
del person.price