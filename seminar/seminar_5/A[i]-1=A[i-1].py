#  В файле находится N натуральных чисел,
# записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

with open('file.txt' ,'r')as file:
    numbers = file.readline()
print(*numbers)
numbers = list(map(int, numbers.split()))
num = [print(numbers[i] - 1) for i in range(1, len(numbers)) if numbers[i] - 1 != numbers[i - 1]]
