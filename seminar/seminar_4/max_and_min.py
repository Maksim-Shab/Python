# Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве разделителя используйте пробел.

some_str = input()
int_list = list(map(int, some_str.split()))
print(max(int_list))
print(min(int_list))
