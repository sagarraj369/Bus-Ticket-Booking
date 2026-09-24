#Bus Ticket printing

print("*******************************************************************************************************************************************************")
list = ['male','female','sn','others']
print(list)

gender = (input("Enter the your gender:- "))
while True:
    try:
        age = int(input("Enter the age:- "))
        break
    except ValueError:
            print(" ")

print("_____________________________________________________________________________________________________________________________________________________")


if gender=='male':
    print('okay')
    if age>=6:
        print("10/-")
    elif age<6:
        print("5/-")


elif gender=='female':
    print('okay')
    if gender=='female':
        print("free")


elif gender=='sn':
    print('okay')
    if age>75:
        print("7/-")
    elif age==75:
        print("7/-")
    elif age<75:
        print("10/-")
        print(" ")
        print("10 Rupees, Because your age is ",age)

   
elif gender=='others':
    print('okay')
    if age in range(1,150):
        print("9/-")
    


else:
    print("Enter the listed gender only") 

print("________________________________________________________________________________________________________________________________________________________")

from datetime import datetime
now = datetime.now()
print("Time:",
      now.strftime("%H:%M:%S"))

from datetime import datetime
print("Date: " + datetime.now().strftime("%d-%m-%y"))


print("******************************************************************Thank you*****************************************************************************")
while True:
    try:
        a = int(input("Enter any number to Exit:- "))
        break
    except ValueError:
            print(" ")

print("Thank you")