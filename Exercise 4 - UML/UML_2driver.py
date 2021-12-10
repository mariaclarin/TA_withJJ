from UML_2class import *

def main():
    print("You have created a new cylinder with the default data below:")
    new = Cylinder(1.0, "red", 1.0)
    print(f"Radius : {new.getRadius()}")
    print(f"Height : {new.getHeight()}")
    print(f"Color : {new.getColor()}")
    print(f"Area : {'{:.2f}'.format(new.getArea())}")
    print(f"Volume : {'{:.2f}'.format(new.getVolume())}")
    print()

    newCylinder = input("Would you like to change the data of the cylinder? (Yes/No) : ")
    if newCylinder == "Yes" or newCylinder == "yes" :
        newrad = float(input("Input desired radius : "))
        newheight = float(input("Input desired height : "))
        newcolor = str(input("Input desired color : "))
        print()
        new.setRadius(newrad)
        new.setHeight(newheight)
        new.setColor(newcolor)
        print("Here is the updated cylinder data:")
        print(f"Radius : {new.getRadius()}")
        print(f"Height : {new.getHeight()}")
        print(f"Color : {new.getColor()}")
        print(f"Area : {'{:.2f}'.format(new.getArea())}")
        print(f"Volume : {'{:.2f}'.format(new.getVolume())}")
    elif newCylinder == "No" or newCylinder == "no" :
        print("That's it, thank you for running me i guess.")
    
main()
