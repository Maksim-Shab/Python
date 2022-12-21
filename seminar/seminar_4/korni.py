# Найти корни квадратного уравнения Ax**2 + Bx + C = 0 двумяспособами:
# 1) с помощью мат формул нахождения корней квадр уровнения
# 2) с помощьюддополнит бтблтотек Python
import math
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
# if a == 0:
#     print('А должно быть больше 0.')
# else:
#     discr = pow(b, 2) - 4 * a * c
#     print(f'Дискриминант = {discr}')
#     if discr == 0:
#         x = -b / (2 * a)
#         print(f'x = {x}')
#     elif discr > 0:
#         x1 = (-b - math.sqrt(discr)) / (2 * a)
#         x2 = (-b + math.sqrt(discr)) / (2 * a)
#         print(f'x1 = {x1} \nx2 = {x2}')
#     else:
#         print('Дискриминант меньше 0, уравнение не имеет решений.')

import sympy
x = sympy.Symbol('x')
print(sympy.solve(a * x ** 2 + b * x + c))
