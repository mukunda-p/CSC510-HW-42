import math
import time

def square(s):
    #Area of square is side*side
    return s*s

def rectangle(l,b):
    #Area of breadth is length*breadth
    return l*b

def circle(r):
    #Area of Circle is Pi*radius*radius*
    return math.pi*r*r

def cube(s):
    #Volume of Cube is side*side*side
    return s*s*s

def cuboid(l,b,h):
    #Volume of Cuboid is length*breadth*height
    return l*b*h

def cylinder(r,h):
    #Volume of Cylinder is Pi*radius*radius*height
    return math.pi*r*r*

T= int(input("Number of shapes:"))

for i in range(T):
    
    print()
    print("Select shape ")
    print("1.Square")
    print("2.Rectangle")
    print("3.Circle")
    print("4.Cube")
    print("5.Cuboid")
    print("6.Cylinder")
    
    choice = input("Enter choice(1/2/3/4/5/6):")
    
    if choice == '1':
        side=int(input("Enter length of square: "))
        print("Area of Square with side = ",square(side))
        
    elif choice == '2':
        length=int(input("Enter length: "))
        breadth=int(input("Enter breadth: "))
        print("Area of Rectangle = ",rectangle(length,breadth))

    elif choice == '3':
        radius=int(input("Enter length of radius: "))
        print("Area of Circle = ",circle(side))
 
    elif choice == '4':
        side=int(input("Enter length of cube: "))
        print("Volume of Cube = ",cube(side))

    elif choice == '5':
        length=int(input("Enter length: "))
        breadth=int(input("Enter breadth: "))
        height=int(input("Enter height: "))
        print("Volume of Cuboid = "+cuboid(length,breadth,height))

    elif choice == '6':
        radius=int(input("Enter length of radius: "))
        height=int(input("Enter height: "))
        print("Volume of Cylinder = ",cylinder(radius,height))
    
    else:
        print("Invalid input")


time.sleep(2) # For stopping python.exe to close immediately.
    
    




