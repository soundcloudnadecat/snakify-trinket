import math

name = input("What is your name? ")
poolShape = input("What is the shape of your pool? ")
length = int(input("Length of a side: "))
width = int(input("Width of a side: "))
depth = int(input("Depth of a wall: "))

if poolShape == "rectangle" or poolShape == "square":
    print(name + ", you will need", (length * width * depth) * 7.5, "gallons of water.")
elif poolShape == "circle":
    print(name + ", you will need", (((math.pi * width) ** 2) * depth) * 5.875, "gallons of water.")
else:
    print("Your pool shape options are: rectangle, square, or circle.")