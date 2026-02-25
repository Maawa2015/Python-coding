lower=int(input("enter the lower bound: "))
upper=int(input("enter the upper bound: "))


for i in range(lower,upper+1):
    if i> 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i,end=" ")
