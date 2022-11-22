mas = [1,8,14,34,3,2,25,6,13,7,4,23,10]
n = len(mas)
first = mas[0]
second = mas[0]
i = 0
while (i < n):
    if (mas[i] > first):
        second = first
        first = mas[i]
    if (mas[i] > second):
        if (mas[i] != first):
            second = mas[i]
    i = i + 1        
print(mas.index(first), mas.index(second))