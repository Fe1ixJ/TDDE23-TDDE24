def foreach(func, lst):
    return [func(element) for element in lst]

print(foreach(lambda x: x**3, [1, 2, 3, 4, 5]))

def f(x):
    return x+10

def g(y):
    return y*2 +7

def compose(f, g):
    return lambda x: f(g(x))

h = compose(f, g)
print(h(2))

def repeat(func, n):
    return lambda x: func(func(func(x)))

square_thrice = repeat(lambda x: x**2, 4)
print(square_thrice(3))

