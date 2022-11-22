# numbers = []
# for _ in range(5):
#     n = int(input())
#     numbers.append(n)
# max = numbers[0]
# for el in numbers:
#     if el > max:
#         max = el
# print(max)

maxx = int(input())
for _ in range(4):
    n = int(input())
    if n > maxx:
        maxx = n
print(maxx)

# print(max(list(map(int, input().split(', ')))))