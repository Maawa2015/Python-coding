def tringlearea(base, height):
    area = (base*height)/2
    return area

def squrearea(side):
    area = side **2
    return area

def retanglearea(length,width):
    area = length * width
    return area

def circlearea(radius):
    area = 3,14159 *radius ** 2

print("AREA CALCULATER")
print("CHOOSE A SHAPE")
print("1. tringle")
print("2. squre")
print("3. retangle")
print("4. circle")

choice= ("enter your choice from 1/2/3//4: ")

if choice == 1:
    b = float(input("enter the base of tringle: "))
    h = float(input("enter the height of tringle: "))
    print("the area of tringle is: "tringlearea(b,h))

elif choice == 2:
    s= float*(input("enter the side of squre: "))
    print("the area of squre is: "squrearea(s))

elif choice == 3:
    l=float("dnter the length of retangle: ")
    w=float(int(" enter the weidth of retangle: "))
    print(" the area of retangle is: "retanglearea(l,w))

elif choice == 4:
    r=float(input("enter the radius of circle: "))
    print(" the area of circle is: "circlearea(r))


else:
    print("invalid input")