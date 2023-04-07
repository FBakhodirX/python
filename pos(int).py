a = int(input("Enter a positive integer: "))
i = int(1)
for n in range(a):
    if a % i == 0 and i <= a:
        print(f"{i} is a factor of {a}")
        i= i + 1
    else :
        i = i + 1 
