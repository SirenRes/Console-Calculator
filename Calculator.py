
import datetime

counter = 1

def sumit(param1, param2):
    return param1 + param2

def subtraction(param1, param2):
    return param1 - param2

def multiply(param1, param2):
    return param1 * param2

def divide(param1, param2):
    return param1 / param2

def checkerror():
    global counter
    while True:
        try:
            param1 = float(input(f"What's the {counter}. number?: "))
        except ValueError as log:
            print("Calculators calculate numbers, nothing else.")
            continue
        else:
            counter += 1
            return param1
    
def display(param1, param2, param3, param4):
    print(f"{param1} {param2} {param3} = {param4(param1, param3)}")

def entry():
    db = {
        "+": sumit,
        "-": subtraction,
        "*": multiply,
        "/": divide,
    }
    first = checkerror()
    if first:
        print("+\n-\n*\n/")
        while True:
            try:
                operation = input("Pick an operation: ")
                store = db[operation]
            except KeyError as log2:
                print("Please choose one of the operations specified there.")
            else:
                break

        second = checkerror()
        if second:
            display(first, operation, second, store)
        else:
            second = checkerror()
    else:
        first = checkerror()


entry()
