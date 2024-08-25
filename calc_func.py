# addition :

def do_addition(a : int,b: int):
    return a + b

def do_subtraction(a : int , b: int):
    return a -b
def do_division(a,b):
    try :
        return a/b
    except ZeroDivisionError as e :
        return "Can not divide by zero ."