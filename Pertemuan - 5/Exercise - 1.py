def print_identity():
    print("---------------------")
    print("|   Elysia Angana   |")
    print("|     Jakarta       |")
    print("---------------------")


def print_identity():
    print("---------------------")
    print("|   Elysia Angana   |")
    print("|     Jakarta       |")
    print("---------------------")

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def modulus(a, b):
    return a % b


print_identity()
print()
while True:
    menu = input("Enter Menu (+|-|/|*|%|stop): ")

    if menu == "stop":
        print("Program stopped. Thank you for using my program.")
        break

    value1 = int(input("Enter Value 1: "))
    value2 = int(input("Enter Value 2: "))


    if menu == "+":
        result = tambah(value1, value2)
        print("The result of addition", value1, "+", value2, "is", result)
        
    elif menu == "-":
        result = kurang(value1, value2)
        print("The result of subtraction", value1, "-", value2, "is", result)

    elif menu == "*":
        result = kali(value1, value2)
        print("The result of multiplication", value1, "*", value2, "is", result)

    elif menu == "/":        
        result = bagi(value1, value2)
        print("The result of division", value1, "/", value2, "is", result)

    elif menu == "%":
        result = modulus(value1, value2)
        print("The result of modulus", value1, "%", value2, "is", result)

    else:
        print("Invalid menu!")