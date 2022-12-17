import view
import import_date
import export_date

def main():
    number_mode = view.modes()
    if number_mode == 0:
        import_date.import_data()
    elif number_mode == 1:
        export_date.export_data()
    else:
        view.none_mode()
        