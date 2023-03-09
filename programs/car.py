repeat = 1
car_started = False
while repeat == 1:
    command = input('car > ')
    if command == 'start':
        if car_started:
            print("Car is already started!")
        elif not car_started:
            car_started = True
            print("Car started!")
    elif command == 'stop':
        if not car_started:
            print("Car is already stopped!")
        elif car_started:
            car_started = False
            print('Car stopped.')
    elif command == "help":
        print("""
start - starts the car
stop - stops the car
quit - returns to Python COM System
""")
    elif command == "quit":
        exit = input('Are you sure you want to quit the car game? (Y/N)')
        if exit == "Y" or "y":
            break
        else:
          pass