import csv
import view

def import_data():
    data = [view.import_mode()]

    with open('db.csv', 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
    
    with open('db.csv', 'r', encoding='utf-8') as f:
        print('\nДанные добавлены.\n\nНиже полный список данных:\n\n' + f.read())
