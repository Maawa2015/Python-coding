a=int(input("ENTER THE SPEED OF FIRST CYCLIST: "))
b=int(input("ENTER THE SPEED OF SECOND CYCLIST: "))
c=int(input("ENTER THE SPEED OF THIRD CYCLIST: "))

avarage = (a + b+ c) / 3
print("avarage speed:", avarage)

if a < avarage:
    print("the first cyclist speed is slower")
if b < avarage:
    print("the second cyclist speed is slower")
if c < avarage:
    print("the third cyclist speed is slower")