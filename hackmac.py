#!/usr/bin/enc python
import os

min = 0
max = 0
c = 1

while c > 0:
    os.system("clear")
    print("+------------------------------+")
    print("|       Hackmac by Abcd        |")
    print("+------------------------------+")
    print("| Exit ................... [0] |")
    print("+------------------------------+")
    print()
    print("Your choice: ", end='')
    try:
        c = int(input())
    except:
        c = 99
        print("Please enter a valid integer [",min,";",max,"]")
        print("Press enter to continue")
        _ = input()
    

print("Thank you for using Hackmac. Good bye!")
