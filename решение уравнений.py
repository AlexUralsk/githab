from math import *
a, b, c = float(input()), float(input()), float(input())
d = pow(b, 2) + 4 * a * c

if d < 0:
    print('Уравнение не имеет  решения')
if d > 0:
    x1 = (-b + sqrt(d))/(2 * a)
    x2 = (-b - sqrt(d))/(2 * a)
print('x1 =', x1)
print('x2 =', x2)
if d == 0:
    x1 = (-b )/(2 * a)
    print('x1 =', x1)