# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите первое число: '))
# if num1 ** 2 == num2 or num2 ** 2 == num1:
#     print('да')
# else:
#     print('нет')

num1, num2 = map(int, input().split(', '))
# num1 = int(some_str[0])
# num2 = int(some_str[1])
if num1 ** 2 == num2 or num2 ** 2 == num1:
    print('да')
else:
    print('нет')
