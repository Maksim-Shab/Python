# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# some_list = [2, 3, 5, 9, 3]
# summ = 0
# for index in  range(len(some_list)):
#     if index % 2 != 0:
#         summ += some_list[index]
# print(summ)




# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# some_list = [2, 3, 4, 5, 6]
# last = len(some_list) - 1
# rezult_list = []
# for ind in range(0, int((len(some_list)/2)+1)):
#     summ = some_list[ind] * some_list[last]
#     last -= 1
#     rezult_list.append(summ)
# print(rezult_list)




# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# some_list = [1.1, 1.2, 3.1, 5, 10.01]
# max = 0
# min = some_list[0]
# for ind in range(len(some_list)):
#     if some_list[ind] % 1 != 0:
#         num = round(some_list[ind] % 1, 2)
#         if max < num:
#             max = num
#         if min > num:
#             min = num
# print(max - min)




# Напишите программу,
# которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число: '))
rezult_list = []
n = 0
while num > 0:
    n = num % 2
    num //= 2
    rezult_list.insert(0, n)
print(rezult_list)