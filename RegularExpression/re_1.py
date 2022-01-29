import re

a = re.compile("dog")
tel_pattern = re.compile(r"^\d\(\d{3}\)\d{3}-\d{2}-\d{2}$")
ph_list = ["8(775)55534-89", "8(999)555-34-89", "8(878)888-34-89"]
nomer_telephon = "8(555)555-34-89"
f = a.findall("My dog name is doggy")
f1 = a.findall("I have a dog")
f2 = a.findall("ket na kutak dog")
print(f, f1, f2)
for tel in ph_list:
    tph = tel_pattern.findall(tel)
    print(tph)

def mydec(x=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            res = res * x
            return f'входные {args[0] + args[1]} и еще умножим на {x} = {res}'
        return wrapper
    return decorator




@mydec(3)
def add(x,y):
    return x+y

s = add(2,5)

print(s)
add = lambda x,y: x*y

def add2(x,y):
    return x+y

print(add(2,4))
print(add2(2,4))

list_a =[]
def some_function(some_arg: list_a):
    some_arg.append(1)
    return some_arg

print(some_function(list_a))
print(some_function(list_a))
print(some_function(list_a))


some_list = [1,4,67,"l",3,6,3,5, "d","d"]
print(list(filter(lambda x: isinstance(x, str), some_list)))

some = False

result = 1 if some else 0
print(result)


#Замыкание

def outher():
    s = 3
    def inner(k):
        x = s ** k
        return x
    return inner

d = outher()
c = d(3)
print(c)
c1 = d(4)
print(c1)