preambula = '''
               Принцип Барбары Липски.
               Дочерний класс может заменить родительский.
               В нашем случае это не работает.
               
               Вот что нужно сделать:
               Сделать классы с единым интерфейсом
               - задаем формат данных в инициализатор               
               - amount прописываем во всех классах
            '''

class Animal:
    def __init__(self, *args):
        self.attributes = {'name': args[0], 'age': args[1]}

    def eat(self, **kwargs):
        amount = kwargs['amount']
        if amount > 0.3:
            print("Не могу есть так много")
        else:
            print("Поел какойто еды")

class Cat(Animal):
    def __init__(self, *args):
        super(Cat, self).__init__(*args)

    def eat(self, **kwargs):
        amount = kwargs['amount']
        if amount > 0.3:
            print("Не могу есть так много")
        else:
            print("Поел какойто кошачей еды")


class Dog(Animal):
    def __init__(self, *args):
        super(Dog, self).__init__(*args)

    def eat(self, **kwargs):
        amount = kwargs['amount']
        if amount > 0.3:
            print("Не могу есть так много")
        else:
            print("Поел какойто собачей еды")


tuzik = Dog('Tuzik', 3)
bobik = Dog('Bobik', 2)
murka = Cat("Murka", 4)
murka.eat(amount=0.2)
egik = Animal('Egik', 3)
egik.eat(amount=0.7)

animals = (tuzik, bobik, murka, egik)

for animal in animals:
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])



print(preambula)