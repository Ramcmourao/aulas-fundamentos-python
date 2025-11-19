'''
Daniel Afonso
Alexandra Sousa
Victor Medeus
'''

from time import sleep

print("----------- Welcome to the DRAW FORMS 1.O -----------\n")
option = ""
figure = "*"
space = " "
ctree = 5
while True:
    ctree = 5
    print("=== MENU ===")
    print("[ 1 ] DRAW RIGHT LADDER")
    print("[ 2 ] DRAW LEFT LADDER ")
    print("[ 3 ] DRAW CHRISTMAS TREE X")
    print("[ 4 ] DRAW X")
    print("[ 0 ] LEAVE\n")
    sleep(0.3)
    option = int(input("Option:\n--> "))
    if(option == 1):
        for c in range (0,5):
           print(figure+(figure*c))
        sleep(0.5)
        input()
        input()
    elif (option == 2):
        sleep(0.5)
        for c in range (0,5):
            print(space * (ctree) + (figure + (figure * c)))
            ctree -= 1
        input()
        input()
    elif (option == 3):
        sleep(0.2)
        for c in range(0,9,2):
            print(space * (ctree) + (figure+(figure*c)))
            ctree -= 1
        input()
        input()
    elif (option == 4):
        sleep(0.2)
        for c in range(0, 5):
            i = ctree - 1 - c
            nospace = ""
            for k in range(0, 5):
                if k == c or k == i:
                    nospace += figure
                else:
                    nospace += space
            print(nospace)
        input()
        input()
    elif (option == 0):
        print()
        print("Leaving program", end=".")
        sleep(0.2)
        print(end=".")
        sleep(0.5)
        print(end=".")
        break
    else:
        print("Choose a valid option!")
        continue
