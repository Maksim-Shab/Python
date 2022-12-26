import random

count = []
def anekdot():
    with open('file.txt', 'r', encoding='utf-8') as text:
        some_list = text.readlines()
        if len(count) == len(some_list):
            count.clear()
        rand_num = random.randint(0, len(some_list)-1)
        if rand_num in count:
            while rand_num in count:
                rand_num = random.randint(0, len(some_list)-1)   
            count.append(rand_num)
            return some_list[rand_num] 
        elif rand_num not in count:
            count.append(rand_num)
            return some_list[rand_num]