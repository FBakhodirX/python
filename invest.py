def invest(amount, rate, years):
    for  n in range(years):
        a = float(amount * (1+rate) )
        amount = a
        print(f"year {n+1} : ${amount:,.2f}")
        
b = invest(100, .05 , 3) 
