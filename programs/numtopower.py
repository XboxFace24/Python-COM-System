repeat = 1
while repeat == 1:
    number_one = input("Number: ")
    if number_one == "!quit":
        break
    number_two = input("This number to what power? ")
    if number_two == "!quit":
        break
    print(float(number_one) ** float(number_two))