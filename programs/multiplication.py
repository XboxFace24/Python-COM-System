repeat = 1
while repeat == 1:
    (number_one) = input("First number: ")
    if number_one == "!quit":
        break
    (number_two) = input("Second number: ")
    if number_two == "!quit":
        break
    print(float(number_one) * float(number_two))