number_list = [1, 2, 3, 4, 5]
str_list = ['one', 'two', 'three', 'four', 'five']
translate_list = {}
for i, j in zip(str_list, number_list):
    translate_list[j] = i
print(translate_list)