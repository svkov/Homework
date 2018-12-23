# 1
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


from functools import reduce

factorial = lambda n: reduce(lambda a, b: a * b, list(range(1, n + 1)))

# 2
# also, you can do it in one line
a = list(range(5, 16))
b = filter(lambda x: x % 2 == 0, a)
c = map(lambda x: x * x, b)
d = reduce(lambda a, b: a * b, c)


# 3
def composition(f, g):
    # using star because g can take more than one argument
    return lambda *x: f(g(*x))


# 4
def optional_introduce(func):
    def f(*x, introduce=False, **args):
        if introduce:
            print(func.__name__) # name of function
        return func(*x)
    return f