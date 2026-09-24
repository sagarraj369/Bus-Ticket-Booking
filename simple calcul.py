def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

while(True):
    print("### simple calculator ###")
    print("1. add")
    print("2. sub")
    print("3. mult")
    print("4. Quit")

    choice = int(input("Enter the above four choice only:- "))
    print("You Enter-->>", choice)

    if choice in {1, 2, 3}:
        a = int(input("Enter the first number:- "))
        b = int(input("Enter the second number:- "))

    if choice==1:
        print("Result:",add(a, b))

    elif choice==2:
        print("Result:",sub(a, b))

    elif choice==3:
        print("Result:",mul(a, b))

    elif choice==4:
        print("Quitting...")
        break

    else:
        print("Invaild Choice. Try again!")
