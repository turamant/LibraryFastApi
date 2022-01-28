class Singl:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singl, cls).__new__(cls)
        return cls.__instance

    def __init__(self, card):
        self.foo = 200
        self.x = 1
        self.card = card


def pizdec():
    print("ket na kutak")

n = Singl(890)
Singl.piki = pizdec()
n.piki
p = Singl("900")

n.px = "Stroka"
print(id(n))
print(id(p))
print((p.px))
print(p.card)
print(n.__class__)
print(p.__class__)
print(type(p))
print(p.__dict__)
print(n.__dict__)
z = getattr(p, 'card')
print(z)
print(Singl.__class__)
for k,v in Singl.__dict__.items():
    print(k,':',v)

print(Singl.__bases__)



