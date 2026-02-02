m= int(input("enter your mark: "))

if m < 33:
    print("GRADE: F")
elif 33<= m <= 39:
    print("GRADE: D")
elif 40<= m <= 49:
    print("GRADE: C")
elif 50<= m <= 59:
    print("GRADE; B")
elif 60<= m <= 69:
    print("GRADE: A-")
elif 70<= m <= 79:
    print("GRADE: A")
elif 80<= m <= 100:
    print("GRADE: A+")
else:
    print("invalid input!")
