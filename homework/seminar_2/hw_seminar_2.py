                    # Задача № 14
# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num = input('Введите число: ')
# summ = 0
# for i in range(len(num)):
#     if num[i] == ',' or num[i] == '.' or num[i] == '-':
#         continue
#     else:
#         summ += int(num[i])
# print('Сумма цифр =', summ)



                    # Задача № 15
# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('Введите число: '))
# rezult = []
# x = 1
# for i in range(1, num + 1):
#     x = x * i
#     rezult.append(x)
# print(rezult)



                    # Задача № 16
# Задайте список из n чисел последовательности (1 + 1 / n) ** n
# и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

# n = int(input('Введите число: '))
# summ = 0
# l = {}
# for i in range(1, n + 1):
#     summ += (1 + 1/i)**i
#     l[i] = round((1 + 1/i)**i, 2)
# print('Для n =',n,l)
# print('Сумма:', round(summ, 2))



                    # Задача № 18
# Реализуйте алгоритм перемешивания списка.

from random import shuffle
from random import randint

num = int(input('Укажите длину списка: '))
l = []
for i in range(num):
    l.append(randint(1, 99))
print('Исходный список:',l)
shuffle(l)
print('Список после перемешивания:',l)