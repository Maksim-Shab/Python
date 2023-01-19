# class Auto:
#     # атрибуты класса
#     auto_name = "Lexus"
#     auto_model = "RX 350L"
#     auto_year = 2019

#     # методы класса
#     def on_auto_start(self):
#         print(f"Заводим автомобиль")
#     def on_auto_stop(self):
#         print("Останавливаем работу двигателя")


# a = Auto()
# print(a)
# print(type(a))
# print(a.auto_name)
# print(Auto.auto_name)
# a.on_auto_start()
# a.on_auto_stop()
# Auto.auto_name = 'audi'
# print(a.auto_name)


# class Auto:

#     # атрибуты класса
#     auto_count = 0

#     # методы класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1


# a =Auto()
# print(Auto.auto_count)
# a.on_auto_start('Audy', 'rs6', '2019')
# print(Auto.auto_count)
# b =Auto()
# b.on_auto_start('BMW', 'M5', '2020')
# print(Auto.auto_count)
# print(a.auto_name)
# print(b.auto_year)



# class Auto:
#     auto_count = 0

#     def __init__(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1

# a = Auto('Volvo', 'x90', 2015)
# print(a.auto_year)



# class Little_Bell():
#     def sound(self):
#         print('ding')

# bell = Little_Bell()
# bell.sound()



# class Button():
#     def __init__(self):
#         self.count = 0

#     def click(self):
#         self.count += 1

#     def click_count(self):
#         return self.count

#     def reset(self):
#         self.count = 0

# button = Button()
# button.click()
# button.click()
# print(button.click_count())
# button.click()
# print(button.click_count())

# b = Button()
# b.click()
# print(b.click_count())



# class Balance():
#     def __init__(self):
#         self.left = 0
#         self.right = 0

#     def add_left(self, num: int):
#         self.left += num

#     def add_right(self, num: int):
#         self.right += num

#     def result(self):
#         x = self.right
#         y = self.left
#         if x > y:
#             print('R')
#         elif x < y:
#             print('L')
#         else:
#             print('=')

# balance = Balance()
# balance.add_left(5)
# balance.add_right(5)
# balance.result()



# class OddEvenSeparator():
#     def __init__(self):
#         self.list_num = []
    
#     def add_number(self, num: int):
#         self.list_num.append(num)
        
#     def even(self):
#         # list_even = []
#         # for i in self.list_num:
#         #     if i % 2 == 0:
#         #         list_even.append(i)
#         # return list_even        
#         return list(filter(lambda x: not x % 2, self.list_num))

#     def odd(self):
#         # list_even = []
#         # for i in self.list_num:
#         #     if i % 2 != 0:
#         #         list_odd.append(i)
#         # return list_odd   
#         return list(filter(lambda x: x % 2, self.list_num))
             
# separator = OddEvenSeparator()
# separator.add_number(2)
# separator.add_number(3)
# separator.add_number(5)
# separator.add_number(1)
# separator.add_number(4)
# print(separator.even())
# print(separator.odd())



# class BigBell():
#     def __init__(self):
#         self.count = 0

#     def sound(self):
#         self.count += 1
#         if self.count % 2:
#             print('ding')
#         else:
#             print('dong')

# bell = BigBell()
# bell.sound()
# bell.sound()
# bell.sound()
# bell.sound()
# bell.sound()



class MinMaxWordFinder():
    def __init__(self):
        self.text = []

    def add_sentence(self, text: str):
        text_list = text.split()
        self.text.extend(text_list)

    def shortest_words(self):
        min = len(self.text[0])
        for item in self.text:
            if min > len(item): min = len(item)      
        short_words = []
        for item in self.text:
            if len(item) == min: short_words.append(item)
        short_words.sort()
        return short_words

    def longest_words(self):  
        maxx = len(self.text[0]) 
        for item in self.text:
            if maxx < len(item): maxx = len(item)      
        long_words = []
        for item in self.text:
            if len(item) == maxx:
                if not item in long_words: long_words.append(item)
        long_words.sort()
        return long_words


finder = MinMaxWordFinder()
finder.add_sentence('hello abc asdfg world')
finder.add_sentence('def asdf adf qwert hello')
print(finder.shortest_words())
print(finder.longest_words())


