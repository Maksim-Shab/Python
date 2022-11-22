num = int(input('Введи число кратное 5 и 10 или 15, но не 30: '))
if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
    print('yes')
else:
    print('no')