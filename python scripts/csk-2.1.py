#python3
#countersink pilot calculator
#Version 2.1

#print("   ___            _               ")
#print("  / _ \ _ __ __ _/ |___ _ __ ___  ")
#print(" | | | | '__/ _` | / __| '_ ` _ \ ")
#print(" | |_| | | | (_| | \__ \ | | | | |")
#print("  \___/|_|  \__, |_|___/_| |_| |_|")
#print("            |___/                 ")
#print("")
#print("")
#print("")

def csk():
    small = float(input("Enter Inside: "))
    big = float(input("Enter Outside size: "))
    result = big - ((big - small) * 0.75)
    print("")
    print("Countersink Pilot Is " + str(result) + "mm")
    print("")
    print("")
    stop = int(input("Enter 1 To Continue Or 2 To Quit: "))
    print("")
    while stop == (1):
        csk()
        break

    else:
        print("")
        print("Good Bye ....")

csk()