#Hole distance
thk = float(input("Enter Material thickness:  "))
rad = float(input("Enter Bend Radius:  "))
hole = (2 * thk) + rad  #formula for 1.0mm or less
slot = (2.5 * thk) + rad
if thk <= 1:
    print("Closest to fold for hole edge is:  " + str(hole) + "mm")
else:
    print("Closest to fold for hole edge is:  " + str(slot) + "mm")
    print("Minimum flange height is: " + str(slot) + "mm")
