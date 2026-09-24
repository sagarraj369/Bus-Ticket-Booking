print("*********************************************************************************************************************************************************")

from datetime import datetime
now = datetime.now()
print("Time:",
      now.strftime("%H:%M:%S"))

from datetime import datetime
print("Date: " + datetime.now().strftime("%d-%m-%y"))

print("----------------------------------------------------------You are know login--------------------------------------------------------------------------")

a=str(input('Enter your name>> '))
pin = "1234"
trials = 1

while trials<=3:
    input_pin = input(f"trials-{trials} | pin = ")
    trials += 1

    if input_pin == pin:
        print("CORRECT,"*10)
        break
    else:
        print('INCORRECT')


b = input(f"Enter your pin to logout:- {pin}" )

if b==pin:
    print("Exit")
    print("----------------------------------------------------------You are know log/out--------------------------------------------------------------------------")

elif b!=pin:
    print("Pin Inncorrect")

