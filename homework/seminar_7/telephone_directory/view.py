def modes():
    inp = int(input('Выберите режим работы:\n0 - импорт(ввод) данных, 1 - экспорт(поиск) данных: '))
    return inp


def export_mode():
    surname_data = input('Введите искомую фамилию: ')
    return surname_data


def import_mode():
    name = input('Введите новую "Фамилю": ')
    surname = input('Введите новое "Имя": ')
    phon = input('Введите новый "номер телефона": ')
    new_data = [name, surname, phon]
    return new_data


def none_mode():
    print('Введенны не корректные данные. Попробуйте ещё раз.\n')


def structure_read():
    structure_data = int(input('Выберите структуру вывода дынных:\n0 - в строку, 1 - в столбец: '))
    return structure_data
    