import math as m
import time
def f(x):
        return (1/2)* m.sin( ((x+3)**2)/2 ) * m.log(x+2)

def findRoot( f,start = 0 ):
    ###
    def sign( n :int):
        if (n >= 0):
            return 1
        else:
            return -1
    a = start
    b = 0.005 + a
    while sign(f(a)) == sign(f(b)):
        b+=0.005
    x = None
    epsilon = 1e-11
    y = 1
    while abs( y ) > epsilon:
        x = (a+b)/2
        y = f(x)
        if (sign(f(a)) != sign(f(x)) ):
            b = x
        else:
            a = x
    return x
x = findRoot(f)
print(x)
def TimeFunction(function):
     def wrapped(*args):
         start_time = time.time()
         res = function(*args)
         print(f"res = {res},\ntime below:",end = "")
         print(time.time() - start_time)
     return wrapped

@TimeFunction
def showTimeFindRoot(f):
    return findRoot(f)
showTimeFindRoot(f)
"""Вариант 15
Верно ли, что заданное многозначное натуральное число содержит
хотя бы 3 одинаковые цифры?
Тест 1: 6066, 34353."""

def FindFirstNRoots(function):
        def wrapped ( n):
                res = []
                start = 0
                for _ in range(n):
                        start = findRoot(function,start)
                        yield start
        return wrapped
# декоратор который получает генератор, находящий первые +n корней
@FindFirstNRoots
def F(x):
        return (1/2)* m.sin( ((x+3)**2)/2 ) * m.log(x+2)
FF = FindFirstNRoots(f)
F(2)
for root in FF(2):
        print(root)

def ClownDecorator(function):
        def wrapper(*args):
                print("you start Clown Function")
                res = function(*args)
                print(f"your clown function return {res}")
                print("u are clown")
                return res
        return wrapper


@ClownDecorator
def myF(x):
       print("body")
myF(32)
