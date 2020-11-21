import random
stroka=input("Введите что нибудь:")
calc=2
calc2=0
calc3=0
calc4=1
calc5=0
yslovie=1
alfavite=''
letters=['q', 'w', 'e', 'r', 't', 'y', 'u', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
for i in stroka:
    if calc3>=calc4:
        i=random.choice(letters) #Делает рандомный выбор из списка
        calc2-=1
        calc4+=3
    if yslovie==1:
        print(i)
        calc2+=1
        calc3+=1
    if calc2>=calc:
        calc+=2
        print("новый фрагмент")
