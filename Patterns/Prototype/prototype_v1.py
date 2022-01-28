from copy import deepcopy

from Patterns.Prototype.prototype_abstract import Prototype


class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "knight"
        filename = "{}_{}.dat".format(self.unit_type, level)
        with open(filename, 'r') as parametr_file:
            lines = parametr_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f'Type: {self.unit_type}\n'\
               f'Life: {self.life}\n' \
               f'Speed: {self.speed}\n' \
               f'Attack_Power: {self.attack_power}\n' \
               f'Attack_Range: {self.attack_range}\n' \
               f'Weapon: {self.weapon}\n'

    def clone(self):
        return deepcopy(self)

class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = "archer"
        filename = "{}_{}.dat".format(self.unit_type, level)
        with open(filename, "r") as parametr_file:
            lines = parametr_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f'Type: {self.unit_type}\n'\
               f'Life: {self.life}\n' \
               f'Speed: {self.speed}\n' \
               f'Attack_Power: {self.attack_power}\n' \
               f'Attack_Range: {self.attack_range}\n' \
               f'Weapon: {self.weapon}\n'

    def clone(self):
        return deepcopy(self)





class Barracks:
    def __init__(self):
        self.units = {
            "knight": {
                1: Knight(1),
                2: Knight(2),
            },
            "archer": {
                1: Archer(1),
                2: Archer(2),
            }
        }
    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()  # Клонируем новый объект id()




if __name__=='__main__':
    barrcks = Barracks()
    knights_dict = {}
    for i in range(1000):
        knights_dict[i] = (barrcks.build_unit("knight", 1))
    archer1 = barrcks.build_unit("archer", 2)
    print("[archer1]\n {}".format(archer1))

    del knights_dict[998]

    for k, v in knights_dict.items():
        print(k, ":+", v)





