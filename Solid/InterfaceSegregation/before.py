class Creature:
    def __init__(self, name):
        self.name = name

    def swim(self):
        pass

    def walk(self):
        pass

    def talk(self):
        pass

class Human(Creature):
    def __init__(self, name):
        super(Human, self).__init__(name)

    def swim(self):
        print(f"Меня зовут {self.name}, я умею плавать")

    def walk(self):
        print(f"Меня зовут {self.name}, я люблю ходить пешком")

    def talk(self):
        print(f"Меня зовут {self.name}, я могу говорить")

class Fish(Creature):
    def __init__(self, name):
        super(Fish, self).__init__(name)

    def swim(self):
        print(f"Меня зовут {self.name}, я умею плавать")

class Cat(Creature):
    def __init__(self, name):
        super(Cat, self).__init__(name)

    def swim(self):
        print(f"Меня зовут {self.name}, я умею плавать")

    def walk(self):
        print(f"Меня зовут {self.name}, я люблю ходить пешком")


if __name__=='__main__':
    human = Human("Иван Петров")
    human.swim()
    human.walk()
    human.talk()

    fish = Fish("Акула")
    fish.swim()

    cat = Cat("Барсик")
    cat.walk()
    cat.swim()
    cat.talk()

