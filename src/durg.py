#PYTHON SMALL REVISION

# sorting
students = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 22},
    {'name': 'Charlie', 'age': 28}
]

sorted_students = sorted(students, key=lambda x: x['age'])
print(sorted_students)

#dictonary with lambda function
numb = [1,2,3,4,5]
squ = {num: (lambda x: x**2)(num) for num in numb}


#lambda
numbers = [3,4,5,6,7]

squred = list(map(lambda x: x**2 , numbers))
print(squred)

# generators passwrd generate

import string
import random


def generate(length=6):
    char = string.ascii_letters + string.digits +string.punctuation
    while True:
        passwd = ''.join(random.choice(char) for _ in range(length))
        yield passwd

passwd_gen = generate()
for _ in range(2):
    print(next(passwd_gen))

# decorator
def decor(func):
    def wrap():
        print('nice')
        func()
        print('function')
    return wrap


@decor
def say():
    print('hellow')

say()


#higher order function
def output(operation, x, y):
    return operation(x,y)

def add(x,y):
    return x+y
def sub(x,y):
    return x-y

result = output(add,5,6)

#metaclasses

class Meta(type):
    def __new__(cls, name,bases, dct):
        print('create class', name)
        print('base', bases)
        print('attributes', dct)

        return super().__new__(cls, name,bases,dct)
    

class Myclass(metaclass = Meta):
    x =30
    y=45

    def method(self):