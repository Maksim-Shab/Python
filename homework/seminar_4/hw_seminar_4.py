# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

# num = float(input('Введите число: '))
# if num.is_integer() == True:
#     print('Введите дробное число!')
# else:
#     d = input('Задайте точность: ').split('.')
#     num = str(num).split('.')
#     num[1] = num[1][: ((len(d[1])))]
#     print(float(f'{num[0]}.{num[1]}'))



# Задайте натуральное число N.
# Напишите программу,
# которая составит список простых множителейчисла N.

# num = int(input('Введите число: '))
# some_list = []
# for ind in range(1, num + 1):
#     if num % ind == 0:
#         for j in range(2, ind//2 + 1):
#             if ind % j == 0:
#                 break
#         else:
#             some_list.append(ind)
# print(*some_list, sep=', ')



# Задайте последовательность чисел. 
# Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.

some_list = list(map(int, input('Введите числа через пробел: ').split()))
num = []
new_list = []
for ind in range(0, len(some_list)):
    if some_list[ind] not in num:
        num.append(some_list[ind])
        for j in range(ind + 1, len(some_list)):
            if some_list[ind] == some_list[j]:
                break
        else:
            new_list.append(some_list[ind])
print('Список неповторяющихся элементов: ', *new_list)