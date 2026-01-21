buy=int(input("enter buying price: "))
sell=int(input("enter the selling price: "))

if sell>buy: 

    profit=sell-buy
    print("you made a profit for tk:",profit)
else:
    lose=buy-sell
    print("you made a lose of tk: ",lose)

