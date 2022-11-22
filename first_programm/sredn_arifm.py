numders = [2,5,13,7,6,4]
size = len(numders)
sum = 0
avg = 0
index = 0
while (index < size):
    sum = sum + numders[index]
    index = index + 1
avg = sum / size
print(avg)