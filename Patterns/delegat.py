class Car:
    def engine(self):
        print("Car: call method engine")

    def akkp(self):
        print("Car: call metho akkp")

class User:
    def work(self):
        print("User: собирает машину")

    def remont(self):
        print("User: ремонитирует машину")

class ElectroCar:
    def __init__(self):
        self.Car = Car()

    def engine(self):
        return self.Car.engine()

    def akkp(self):
        return self.Car.akkp()


class MyCar(Car, User):
    pass

mycar = MyCar()
mycar.akkp()
mycar.engine()
mycar.work()
mycar.remont()
print("======"*10)
el_car = ElectroCar()
el_car.engine()
el_car.akkp()

