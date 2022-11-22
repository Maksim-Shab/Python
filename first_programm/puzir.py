mas = [8,14,34,10,7,5,3,2]
n = len(mas)
i = 0
j = 0
ss =0
while(ss<n):
    i=0
    while(i < (n - 1 - ss)):
        j=mas[i]
        mas[i]=mas[i+1]
        mas[i+1]=j
        i=i+1
    ss=ss+1
print(mas)