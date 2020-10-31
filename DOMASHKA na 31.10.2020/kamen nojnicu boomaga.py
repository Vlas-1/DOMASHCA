import random
WinComp=0
WinUser=0
WinNikto=0
kolIgr=int(input("Введите количество игр"))
igru=kolIgr
for i in range(0,kolIgr):
    user=int(input("Выберете Камень-1,Ножницы-2,Бумага-3:"))
    if user==1:
        print("Пользователь-Камень")
        print("самым лучшим решением против вас будет бумага")
    if user==2:
        print("Пользователь-Ножницы")
        print("самым лучшим решением против вас будет камень")
    if user==3:
        print("Пользователь-Бумага")
        print("самым лучшим решением против вас будут ножницы")
    if user>=4:
        print("НЕПРАВИЛЬНО")
    comp=(random.randint(1,3))
    if comp==1:
        print("Комп-Камень")
    if comp==2:
        print("Комп-Ножницы")
    if comp==3:
        print("Комп-Бумага")
    if user==1:
        if comp==2:
            print("Камень давит ножницы")
            WinUser+=1
    if user==1:
        if comp==3:
            print("Бумага накрывает камень")
            WinComp+=1
    if user==1:
        if comp==1:
            print("Два камня уничтожили друг друга")
            WinNikto+=1
    if user==2:
        if comp==1:
            print("Ножницы затупились об камень")
            WinComp+=1
    if user==2:
        if comp==2:
            print("Ножницы разрезали друг друга")
            WinNikto+=1
    if user==2:
        if comp==3:
            print("Ножницы режут камень")
    if user==3:
        if comp==1:
            print("Бумага накрывает камеень")
            WinUser+=1
    if user==3:
        if comp==2:
            print("Ножницы режут бумагу")
            WinComp+=1
    if user==3:
        if comp==3:
            print("Две бумаги слишком беспомошьны")
            WinNikto+=1
print("Пользователь победил",WinUser,"Раз")
print("Комп победил",WinComp,"Раз")
print("Ничья была",WinNikto,"Раз")
        
    

