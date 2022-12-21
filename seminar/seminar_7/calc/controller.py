import model
import operation
import view

def button_click():
    some_str = view.inp()
    some_tuple = operation.op(some_str)
    if some_tuple[2] == '+':
        result = model.summ(some_tuple[0], some_tuple[1])
    elif some_tuple[2] == '-':
        result = model.diff(some_tuple[0], some_tuple[1])
    elif some_tuple[2] == '*':
        result = model.mult(some_tuple[0], some_tuple[1])
    else:
        result = model.div(some_tuple[0], some_tuple[1])
    view.view_data(result)