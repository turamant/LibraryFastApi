preambula = '''
               Принцип Барбары Липски.
               Дочерний класс может заменить родительский.
               В нашем случае это не работает.
               Смотрим файл after.py              
                
            '''

class Animal:
    def __init__(self, attrs):
        self.attributes = attrs

    def eat(self):
        print("Поел какойто еды")

class Cat(Animal):
    def eat(self, amount = 0.1):
        if amount > 0.3:
            print("Не могу есть так много")
        else:
            print("Поел какойто кошачей еды")

class Dog(Animal):
    def eat(self):
        print("Поел какойто собачьей еды")

tuzik = Dog({'name': 'Tuzik', 'age': 3})
bobik = Dog({'name': 'Bobik', 'age': 2})
murka = Cat(("Murka", 4))

animals = (tuzik, bobik)

for animal in animals:
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])

print(preambula)