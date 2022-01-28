class IProduct:
    def release(self):
        pass

class Car(IProduct):
    def release(self):
        print("Легковой автомобиль")


class Truck(IProduct):
    def release(self):
        print("Грузовик")

class IWorkShop:
    def creator(self):
        pass

class WorkCarPlant(IWorkShop):
    def creator(self):
        return Car()

class WorkTruckPlant(IWorkShop):
    def creator(self):
        return Truck()



creator = WorkCarPlant()
car = creator.creator()

creator = WorkTruckPlant()
truck = creator.creator()

car.release()
truck.release()
