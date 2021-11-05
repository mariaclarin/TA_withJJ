def diamondmaker():
    height = eval(input("Enter desired height:"))
    for i in range(height):
        print(" "*(height-i), "*"*(i*2+1))
    for i in range(height-2, -1, -1):
        print(" "*(height-i), "*"*(i*2+1))

diamondmaker()