# num = input('Введите дробное число: ')
# if ',' in num:
#     num = num.split(',')
#     print(num[1][0])
# else:
#     print('нет')


# num = input('Введите дробное число: ')
# if ',' in num:
#     ind = num.index(',')
#     print(num[ind + 1])
# else:
#     print('нет')


num = float(input('Введите дробное число: '))
if num % 1 != 0:
    num = num * 10
    num = int(num)
    print(num % 10)
else:
    print('нет')