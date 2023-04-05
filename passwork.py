kod = 0
while(kod<3):
    a = int(input("Я загадал число от 1 до 10 угадай"))
    if a == 3:
        print("WIns")
        break
    elif a!=a:
        print("You are no Wins")  
    kod = kod + 1    
    print(f"У вас осталось {3 - kod} попыток")  
else:
        print("Вы заблокированы ")