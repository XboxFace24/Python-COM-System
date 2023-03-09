import os
import shutil
import datetime
import random
import time

def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)

print("Python COM System by XboxFace24 GMD")
print("Read the readme.txt file for more info")
com_started = True
curdir = os.getcwd()
dirname = curdir

while com_started:
    command = input(dirname + ' > ')
    if command == "ping":
        print('pong!')
    elif command == "car":
        os.chdir('programs')
        exec(open("car.py").read())
        os.chdir("..")
    elif command == "jimothi99":
        os.chdir('programs')
        exec(open("jimothi99.py").read())
        os.chdir("..")
    elif command == "":
            print("You must type a command!")
    elif command == "quit":
        quit = input("Are you sure you want to quit Python COM System? (Y/N) ")
        if quit == "Y":
            break
        else:
            pass
    elif command == "multiply":
        os.chdir('programs')
        exec(open("multiplication.py").read())
        os.chdir("..")
    elif "len" in command:
        word = command[4:]
        print("Length: " + str(len(word)) + " letters")
    elif command == "add":
        os.chdir('programs')
        exec(open("addition.py").read())
        os.chdir("..")
    elif command == "subtract":
        os.chdir('programs')
        exec(open("subtract.py").read())
        os.chdir("..")
    elif command == "divide":
        os.chdir('programs')
        exec(open("division.py").read())
        os.chdir("..")
    elif command == "help":
        print("""add - opens the addition calculator
car - opens the car game
cd {directory name} - changes directory
copy {factors} - opens a prompt to copy a file (has required factors,
type "help factors" for more info)
countdown {seconds} - counts down a number of seconds specified
datetime now - shows the current date and time
del {filename} - deletes a specified file
dir - lists files in current directory
divide - opens the division calculator
gdrandid - prints a random Geometry Dash Level ID
Note: A lot of the IDs generated lead to levels which
don't exist anymore on the Geometry Dash servers.

Pro tips:
Type "help" followed by the name of a program to see
the program's commands!
Type "help 2" to see the next page of commands!
Type "help factors" for info about command factors!
Also, the only command in calculator programs is '!quit'
Type "cd .." to go back to the previous directory.""")
    elif command == "help 2":
        print("""install {package filename} - installs a package in .py format
(can be used to install updates and custom packages)
jimothi99 - opens the jimothi99 chatbot program
len {word} - prints the length of a word or sentence
mkdir {directory name} - makes a new directory with specified name
move {filename} - opens a prompt to move a specified file from one
directory to another
multiply - opens the multiplication calculator
numtopower - opens the program for raising a number to a specified power.
open pyfile {filename.py} - opens any specified Python file
readtxt {filename} - prints the text of a specified file
rename {filename} - opens a prompt to rename a specified file
rmdir {directory name} - deletes an empty directory
rmtree {directory name} - deletes a specified directory and all contents
ping - replies with 'pong!'

Pro tips:
Type "help" followed by the name of a program to see
the program's commands!
Type "help 3" to see the next page of commands!
Type "help factors" for info about command factors!
Also, the only command in calculator programs is '!quit'
Type "cd .." to go back to the previous directory.""")
    elif command == "help 3":
        print("""quit - exits Python COM System
subtract - opens the subtraction calculator
systemtools - allows you to use system tools, such as resetting
Python COM System.
writetxt {filename} - writes text to a file (has optional factor, type
"help factors" for more info)

Pro tips:
Type "help" followed by the name of a program to see
the program's commands!
Type "help 4" to see the next page of commands!
Type "help factors" for info about command factors!
Also, the only command in calculator programs is '!quit'
Type "cd .." to go back to the previous directory.""")
    elif command == "numtopower":
        os.chdir('programs')
        exec(open("numtopower.py").read())
        os.chdir("..")
    elif command == "help jimothi":
        print("""!stop - quit the jimothi chatbot program
And that's literally the only command in the jimothi program""")
    elif command == "dir":
        dirlist = os.listdir()
        print(dirlist)
    elif "rmtree" in command:
        rmtreename = command[7:]
        shutil.rmtree(rmtreename)
        print("Directory deleted!!")
    elif "mkdir" in command:
        newdirname = command[6:]
        os.mkdir(newdirname)
        print("Directory made!")
    elif "cd" in command:
        dirchange = command[3:]
        os.chdir(dirchange)
        dirname = os.getcwd()
        if "/Python COM System/programs" in dirname:
            print("Warning: Attempting to run programs in this folder with their normal")
            print("commands will cause the command prompt to crash. If you want to run a program")
            print("while in this folder, use the 'open pyfile' command instead.")
    elif "open pyfile" in command:
        pyfile = command[12:]
        exec(open(pyfile).read())
    elif "writetxt" in command:
        if command[9:11] == "-r":
            filename = command[12:]
            f = open(filename, "w")
            print("Type anything into the box, and press enter when done.")
            text = input("")
            f.writelines(text)
            f.close()
            print("Text replaced in " + str(filename) + "!")
        else:
            filename = command[9:]
            if filename in os.listdir():
                print("")
                print("File already exists! If you want to replace text in the file,")
                print('run "writetxt -r {filename}" instead.')
                print("")
            else:
                f = open(filename, "x")
                print("Type anything into the box, and press enter when done.")
                text = input("")
                f.writelines(text)
                f.close()
                print("Text saved to " + str(filename) + "!")
    elif "del" in command:
        filename = command[4:]
        if filename not in os.listdir():
            print("Error: File doesn't exist!")
        else:
            os.remove(filename)
            print("File deleted!")
    elif "readtxt" in command:
        txtfile = command[8:]
        text = open(txtfile).read()
        print(text)
    elif command == "datetime now":
        print(datetime.datetime.now())
    elif "install" in command:
        package = command[8:]
        exec(open(package + ".py").read())
    elif command == "gdrandid":
        print(random.randint(128, 88507182))
    elif "countdown" in command:
        seconds = command[10:]
        countdown(int(seconds))
        print("Countdown done!")
    elif "copy" in command:
        if command[4:] == "":
            print("You must add at least one factor!")
        elif command[5:] == "-f -d":
            filename = input("Source file: ")
            if filename not in os.listdir():
                print("Error: Source file doesn't exist!")
            else:
                dir = input("Destination directory: ")
                shutil.copy2(filename, dir)
                print("Successfully copied " + filename + " to the directory " + dir + "!")
        elif command[5:] == "-f":
            source = input("Source filename: ")
            if source not in os.listdir():
                print("Error: Source file doesn't exist!")
            else:
                destination = input("Destination filename: ")
                shutil.copy(source, destination)
                print("Successfully copied " + source + " to " + destination + "!")
    elif "move" in command:
        source = command[5:]
        if source not in os.listdir():
            print("Error: Source file doesn't exist!")
        else:
            dir = input("Destination directory: ")
            shutil.move(source, dir)
            print("Successfully moved " + source + " to destination!")
    elif "rename" in command:
        if command[7:] not in os.listdir():
            print("Error: File doesn't exist!")
        elif command[6:] == "":
            print("You must specify a file!")
        else:
            old_name = command[7:]
            new_name = input("New name: ")
            if new_name in os.listdir():
                print("Error: There is already a file with this name!")
            else:
                os.rename(old_name, new_name)
                print("Renamed " + old_name + " to " + new_name + "!")
    elif command == "help factors":
        print("""copy {factors}
-f (makes a copy of a specified file)
(Also makes you type in a new name for copied file)
-f -d (copies a file from one directory to another)

writetxt {optional factor} {filename}
-r (replaces text in a file)
(normally, it doesn't let you write text to the file if it already exists)""")
    elif "rmdir" in command:
        dir = command[6:]
        if os.listdir(dir) != []:
            print("Error: Directory not empty! Use rmtree instead.")
        else:
            os.rmdir(dir)
            print("Successfully removed directory!")
    elif command == "systemtools":
        print("Choose an option:")
        print("")
        print("1. Reset Python COM System")
        print("")
        option = input("Option: ")
        if option == "1":
            os.chdir("systemtools")
            exec(open("resetsystem.py").read())
            os.chdir("..")
    else:
        print("Error: Invalid command!")
