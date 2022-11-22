from random import randint

x = randint(0, 100)

count_perebor = 0

for i in range(0,101):
   count_perebor+=1
   if i == x:
        print("Число найдено!")
        break

print("Загаданное число было ", x, " и для его поиска потребовалось ", count_perebor, " итераций." )

count_bin = 1
print('Давай начнем игру - угадай число от 0 до 100')
y = int(input('Введи число'))

while  x!=y:
    if x<y: print("меньше")
    else: print("больше")
    y=int(input())
    count_bin+=1
    
print("Загаданное число было ", x, " и для его поиска потребовалось ", count_perebor, " итераций." )
