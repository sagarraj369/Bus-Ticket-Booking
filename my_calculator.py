#calculator
while True:
    try:
        a = int(input("Enter the First number:- "))
        b = int(input("Enter the Second number:- "))
        
    except ValueError:
        print("Enter the number only ")
        break


    print('x).addition')
    print('y).subtraction')
    print('z).multipication')
    print('s).division')


    d = input('Enter your choice:- ')

    x = a + b  # Addition
    y = a - b  # Subtraction
    z = a * b  # Multipliction
    s = a / b  # Division
    t = a // b

    if d=='x':
        print(x)
    elif d=='y':
        print(y)
    elif d=='z':
        print(z)
    elif d=='s':
        print(s)
    elif d=='t':
        print(t)


else:
    print("Invalid choice")




