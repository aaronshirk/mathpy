from math import sqrt

def func1(x):
    return 2*(x**2) + 7*x - 15


def quad(a,b,c):
    term = sqrt(b**2 - 4*a*c)
    x1 = (-b + term) / (2*a)
    x2 = (-b - term) / (2*a)
    return x1,x2

a1,a2 = quad(2,7,-15)
print(a1, a2)

sol1 = func1(a1)
sol2 = func1(a2)

print(sol1, sol2)