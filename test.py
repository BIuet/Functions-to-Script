import subprocess
def getDirectory():
    """Gets current directory"""
    out = subprocess.run(["ls", "-la"], capture_output=True)
    print(out)

calc = 0

def val():
    """VAL"""
    print("Current value: " + str(calc))

def add():
    """ADD"""
    global calc
    choice = input("Enter a number: ")
    if choice.isnumeric():
        calc += int(choice)
        print(calc)
    else:
        print("Invalid input.")

def sub():
    """SUB"""
    global calc
    choice = input("Enter a number: ")
    if choice.isnumeric():
        calc -= int(choice)
        print(calc)
    else:
        print("Invalid input.")

def mul():
    """MUL"""
    global calc
    choice = input("Enter a number: ")
    if choice.isnumeric():
        calc *= int(choice)
        print(calc)
    else:
        print("Invalid input.")
