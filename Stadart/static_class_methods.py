class Person:
    name = "person"
    city = "Moscow"
    data = ['one']

    def write_data(self, new_data):
        Person.data.append(new_data)

    def read_data(self):
        for i in Person.data:
            print(i)

    @staticmethod
    def write(new_d):
        Person.data.append(new_d)

    @classmethod
    def wrotten(cls):
        cls.data.append("ket nax")

class Man(Person):
    @staticmethod
    def write(new_d):
        print("Man %s" % new_d)

p = Person()
print(id(p))
p.write_data("Kony Aland")
p.write("pepci")
p.wrotten()
p.read_data()

m = Man()
print(id(m))
m.write("Ket")