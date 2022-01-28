from abc import abstractmethod, ABCMeta
from copy import deepcopy

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass

class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)


if __name__=='__main__':
    concrete = Concrete()
    print(concrete)
    print(concrete.clone())