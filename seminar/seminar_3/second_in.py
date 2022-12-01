# Напишите прогр, которая определит
# позицию второго вхождения в списке,
# либо сообщит, что её нет.

some_list = ['qwe','asd','zxc','qwe','erty']

a = input('Введи значение: ')

count = 0
count2 = 0
b = False
for line in some_list:
    count += 1
    if a == line:
        count2 += 1
        if count2 == 2:
            b = True
            print(f'{count}')
if not b:
    print('No')