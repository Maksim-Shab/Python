# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def write_file(st):
    with open('file33.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0,101)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    

def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')




# sum_of_poly = (list_of_poly_1), '+' (list_of_poly_2)




# if len(poly_1) > len(poly_2):
#     help_poly = poly_1
#     poly_1 = poly_2
#     poly_2=help_poly
# poly_1 = poly_1.split(' + ')
# poly_2 = poly_2.split(' + ')
# print(poly_1,poly_2)

# count1 =0
# count2=len(poly_2)-len(poly_1)
# new_poly = ''
# for i in range(count2):
#     new_poly += poly_2[i] + '+'

# ind1 = ''
# ind2 = ''

# for i in range(len(poly_2) - len(poly_1), len(poly_2)):
#     result = 0 
#     if i == len(poly_2) - 1:
#         result += int(poly_1[-1][:-4]+poly_2[-1][:-4])
#         new_poly += str(result) + poly_1[-1][-4:]
#     elif i == len(poly_2) - 2:
#         result += int(poly_1[-2][:-2]+poly_2[-2][:-2])
#         new_poly += str(result) + poly_1[-2][-2:] + ' + ' 
#     else:
#         result += int(poly_1[count1][:-4]+poly_2[count2][:-4])
#         new_poly += str(result) + poly_1[count1][-4:] + ' + ' 
#         count1 += 1
#         count2 += 2
# print(new_poly)



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
print(*new_list)


# for ind in some_list:
#     if some_list.count(ind) == 1:
#         print(ind, end=' ')