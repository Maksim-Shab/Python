# num = int(input())
# if num > 0:
#     for i in range(- num, num):
#         print(i, end=', ')
# else:
#     for i in range(num, -num):
#         print(i, end=', ')
# print(-num)

num = int(input())
print(*list(range(-num ,num +1)), sep = ', ')