import csv
import view


def export_data():
    surname = view.export_mode()
    with open('db.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        s = False
        some_str = ''
        struсt_data = view.structure_read()
        for row in reader:
            for i in range(len(row)):
                if surname == row[i]:
                    s = True
                    if struсt_data == 0:
                        some_str += str(row) + '\n'
                    elif struсt_data == 1:
                        some_str += str(row[i] + '\n' + row[i + 1] + '\n' + row[i + 2] + '\n\n')
                    else:
                        print('Выберите один из вариантов структуры вывода данных.')
        if s == True:
            print('По введенным данным найдены люди:\n' + some_str)
        else:
            print('Люди с такой фамилией не найдены.\n')
