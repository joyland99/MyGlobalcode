def calculate():
    op=input("Which operation do you want to carry out")
    if op in "add,ADD":
        num1=int(input("enter first number"))
        num2=int(input("enter first number"))
        print(num1+num2)
    elif op in "MULTIPLY, multiply":
        num1 = int(input("enter first number"))
        num2 = int(input("enter first number"))
        print(num1 * num2)
    elif op in "SUBTRACT, subtract":
        num1 = int(input("enter first number"))
        num2 = int(input("enter first number"))
        print(num1 - num2)
    elif op in "DIVIDE,divide":
        num1 = int(input("enter first number"))
        num2 = int(input("enter first number"))
        print(num1 / num2)
    else:
        print("invalid operation")



calculate()
