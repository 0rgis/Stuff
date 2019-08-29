#python3.7
#0rg1s pwns th1s
#Hole/Flange distance calculator

def holedge():
    thk = float(input("Enter Material thickness:  "))
    rad = float(input("Enter Bend Radius:  "))
    hole = (2 * thk) + rad  #formula for 1.0mm or less
    slot = (2.5 * thk) + rad  #formula for over 1.0 mm
    if thk <= 1:
        print("")
        print("")
        print("Closest to fold for hole edge is:  " + str(hole) + "mm")
        print("")
        stop = int(input("Enter 1 To Continue Or 2 To Quit: "))
    else:
        print("")
        print("")
        print("Minimum flange height & Closest to fold for hole edge is:  " + str(slot) + "mm")
        print("")
        print("")
        stop = int(input("Enter 1 To Continue Or 2 To Quit: "))
        print("")        
    while stop == (1):
        holedge()
        break
    else:
        print("")
        print("Good Bye ....")
holedge()
