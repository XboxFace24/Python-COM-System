print('You are now talking to jimothi99!')
repeat = 1
while repeat == 1:
    word = input("Send a message: ")
    print("jimothi99: " + word)
    if word == "!stop" or word == "!STOP":
        print("You have stopped talking to jimothi99.")
        break
