#csk calculator

#start working ish lol
small = float(input("Enter Inside:  "))
big = float(input("Enter Outside size:  "))
result = big - ((big - small) * 0.75)
print("Countersink Pilot Is " + str(result) + "mm")
print("")
stop = int(input("Enter 1 To Continue Or 2 To Quit: "))
#quit or continue
if stop == (1):
    print("re run script")#testing if stop, not using print
else:
    print("bye bye")
#end working
    
"""
#start restart
restart = True

while restart:
    #the program
    small = float(input("Enter Inside:  "))
    big = float(input("Enter Outside size:  "))
    result = big - ((big - small) * 0.75)
    print("Countersink Pilot Is " + str(result) + "mm")
    #print("")

    restart = input("Press any key to restart or q to quit!")
    if restart == "q":
        restart = False
#end restart        
"""
