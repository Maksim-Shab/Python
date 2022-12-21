# def even(i):
#     return i % 2 == 0
# Заменяем на lambda i: i % 2 == 0
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(filter(lambda i: i % 2 == 0, some_list))
print(new_list)