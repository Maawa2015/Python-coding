def calculater(choice, a, b):
    if choice == 1:
        return a+b
    elif choice == 2:
        return a-b
    elif choice == 3:
        return a*b
    elif choice == 4:
        if b==0:
            return "Error!division by zero is not allowed."
        return a/b
    return "invalid choice"

print("------------C A L C U L A T E R------------------")
print("1. ADITION")
print("2. subtraction")
print("3. multiplication")
print("4. divition")
print("----------------------------")

choice= int(input("enter the choice(1/2/3/4):"))
a=float(input("enter the first number:"))
b=float(input("enter the second number:"))

result= calculater(choice, a, b)

print("---------------------")
print("RESULT: ",result)
print("-------------------------")
