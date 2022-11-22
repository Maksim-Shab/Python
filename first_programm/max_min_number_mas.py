mas = [8,14,34,3,11,12,2,25,6,13,7,4,23,10]
n = len(mas)
big = mas[0]
little = mas[0]
i = 0
while (i < n):
    if (mas[i] > big):
        big = mas[i]
    if (mas[i] < little):
        little = mas[i]
    i = i + 1        
print(mas.index(big), mas.index(little))