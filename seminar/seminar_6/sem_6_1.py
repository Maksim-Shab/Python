# some_dict = {}
# N = int(input())
# for _ in range(N):
#     line = input()
#     some_dict[line.split()[0]] = line.split()[1:]
#
# M = int(input())
# some_list = [input() for _ in range(M)]
#
# for word in some_list:
#     if word.lower() in some_dict:
#         print(*some_dict[word])
#     else:
#         print('Нет в словаре')

# def arithmetic_operation(operation):
#     if operation == '+':
#         return lambda x, y: x + y
#     elif operation == '-':
#         return lambda x, y: x - y
#     elif operation == '*':
#         return lambda x, y: x * y
#     else:
#         return lambda x, y: x / y
#
#
# operation = arithmetic_operation('/')
# print(operation(1, 4))


# def simple_map(transformation, values: list):
#     return list(map(transformation, values))
#
#
# values = [1, 3, 1, 5, 7]
# print(simple_map(lambda x: x + 5, values))