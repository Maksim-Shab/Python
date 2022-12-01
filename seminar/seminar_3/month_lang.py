# Напишите функцию, которая принимает номер месяца и язык,
# а возвращает его название
# Ввод:
    # print(month_name(3, "en"))
    # March
# Ввод:
    # print(month_name(3, "ru"))
    # Март
x = int(input('Введи номер месяца: '))
y = input('Введин язык вывода(в формате en/ru): ')
def Rezult(num,leng):
    list_en = ('January','February','March','April','May','June','July','August','September','October','November','December')
    list_ru = ('Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь')
    if 0 < num < 13:
        if leng == 'en':
            return list_en[num-1]
        if leng == 'ru':
            return list_ru[num-1]
print(Rezult(x, y))