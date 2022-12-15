# Дан список интов , повторяющихся элементов в списке нет
# Нужно преобразовать это множество в строку ,
# сворачивая соседние по числовому ряду числа в диапазоны
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

some_list = [11,4,5,2,3,9,8,11,0]
some_list.sort()
some_str = str(some_list[0])
iteration = False
for i in range(1, len(some_list)):
    if some_list[i] - 1 == some_list[i - 1]:
        iteration = True
    else:
        if iteration == False:
            some_str += ',' + str(some_list[i])
        else:
            some_str += '-' + str(some_list[i - 1]) + ',' + str(some_list[i])
            iteration = False
if (iteration):
     some_str += '-' + str(some_list[-1])
print(some_str)



# Дана строка ( возможно , пустая ), состоящая из букв A-Z
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку , если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз , он остается без изменений;
# Если символ повторяется более 1 раза ,
# к нему добавляется количество повторений.

# some_list = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'

# def press():
#     new_list = ''
#     count = 1
#     a = False
#     for i in range(len(some_list) - 1):
#         if some_list[i].isdigit():
#             print('Введены не корректные данные')
#             a = True
#             break
#         else:
#             if some_list[i] == some_list[i + 1]:
#                 count += 1
#             else:
#                 if count == 1:
#                     new_list += some_list[i]
#                 else:
#                     new_list += some_list[i] + str(count)
#                     count = 1
#     new_list += some_list[i] + str(count)
#     if a != True:
#         print(new_list)            
# press()
