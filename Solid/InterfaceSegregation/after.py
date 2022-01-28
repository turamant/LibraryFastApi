class Creature:
    def __init__(self, name):
        self.name = name

class SwimmerInterface:
    def swim(self):
        print(f"Меня зовут {self.name}, я умею плавать")

class TalkInterface:
    def talk(self):
        print(f"Меня зовут {self.name}, я могу говорить")

class WalkInterface:
    def walk(self):
        print(f"Меня зовут {self.name}, я люблю ходить пешком")


class Human(Creature, SwimmerInterface, TalkInterface, WalkInterface):
    def __init__(self, name):
        super(Human, self).__init__(name)

class Fish(Creature, SwimmerInterface):
    def __init__(self, name):
        super(Fish, self).__init__(name)

class Cat(Creature, SwimmerInterface, WalkInterface, TalkInterface):
    def __init__(self, name):
        super(Cat, self).__init__(name)

if __name__=='__main__':
    human = Human("Иван Петров")
    human.swim()
    human.walk()
    human.talk()
    print("=="*12)

    fish = Fish("Акула")
    fish.swim()
    print("==" * 12)

    cat = Cat("Барсик")
    cat.walk()
    cat.swim()
    cat.talk()



