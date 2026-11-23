print("ФУНКЦИЯ КАК ТИП ")
print(" ")

print("задание 1 ")
def say_hi():
    print("привет")
other=say_hi 
other()

print("---------------------------------------------------")
print("задание 2 ")
def cube(x):
    return x ** 3 
first = cube 
second = cube 
print(first(2))
print(second(3))

print("---------------------------------------------------")
print("задание 3 ")
def get_five():
    return 5 
print(type(get_five))
print(type(get_five()))

print("---------------------------------------------------")
print("")
print("ФУНКЦИЯ КАК ПАРАМЕТР ФУНКЦИИ")
print("")
print("задание 4 ")
def priv():
    print("hello")
def run(action):
   action() 
run(priv)

print("---------------------------------------------------")
print("задание 5")
def ydv(x):
    return x  * 2 
def apply(action, number):
    return action(number)
print(apply(ydv,6))
print("---------------------------------------------------")
print("задание 6")
def add_ten(x):
    return x + 10

def transform(values, action):
    result = []

    for x in values:
        result.append(action(x))

    return result

print(transform([1, 2, 3], add_ten))

print("---------------------------------------------------")
print("")
print("ФУНКЦИЯ КАК РЕЗУЛЬТАТ ФУНКЦИИ ")
print("")
print("задание 7 ")
def factory():
    def work():
        print("Работает")

    return work

f = factory()
f()
print("---------------------------------------------------")
print("задание 8")
def make_adder(value):
    def add(x):
        return x + value

    return add

adder = make_adder(5)

print(adder(7))
print("---------------------------------------------------")
print("задание 9")
def make_counter():
    count = 0

    def c():
        nonlocal count
        count += 1
        return count

    return c

c = make_counter()

print(c())
print(c())
print(c())