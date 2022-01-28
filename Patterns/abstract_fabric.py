from abc import ABCMeta, abstractmethod


class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def release_engine(self):
        pass

class JapanEngine(IEngine):
    def release_engine(self):
        print("made in Japan motor ")

class RussianEngine(IEngine):
    def release_engine(self):
        print("made russian motor")


class ICar(metaclass=ABCMeta):
    @abstractmethod
    def release_car(self, engine):
        pass

class JapanCar(ICar):
    def release_car(self, engine):
        print("Made in japan car")
        engine.release_engine()

class RussianCar(ICar):
    def release_car(self, engine):
        print("Made in russian car")
        engine.release_engine()

class IWorkPlant(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_car(self):
        pass


class JapanWorkPlant(IWorkPlant):
    def create_engine(self):
        return JapanEngine()

    def create_car(self):
        return JapanCar()


class RussianWorkPlant(IWorkPlant):
    def create_engine(self):
        return RussianEngine()

    def create_car(self):
        return RussianCar()


if __name__=='__main__':
    r_factory = RussianWorkPlant()
    r_engine = r_factory.create_engine()
    r_car = r_factory.create_car()

    r_car.release_car(r_engine)

