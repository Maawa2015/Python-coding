cause = str(input("Do you have medical cause? (yes?no): ")).lower()

if cause == "yes":
    percentage = int(input("Enter the attendence percentage: "))
    if percentage >= 60:
        print ("you are eligible for exam.")
    else:
        print ("you are not eligible for exam. ")
elif cause == "no":
    percentage= int(input("Enter the attendence percentage: "))
    if percentage >= 75:
        print("you are eligible for exam. ")
    else:
        print("you are not eligible for exam.")
else:
    print("invalid input!")
