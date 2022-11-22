mas = [8,14,34,10,7,5,3,2]
n = len(mas)
big = mas[0]
little = mas[0]
i = 0
s = 0
while (i < n):
    if (mas[i] > big):
        big = mas[i]
    if (mas[i] < little):
        little = mas[i]
    i = i + 1 
if(mas.index(big) < mas.index(little)):
    j = mas.index(little)
    p = mas.index(big) + 1
if(mas.index(little) < mas.index(big)):
    j = mas.index(big)
    p = mas.index(little) + 1
while(p < j):
    s = s + mas[p]
    p = p + 1
print(s)