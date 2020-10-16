koors=float(input("Введите курс долларра: "))
stoimostkgkonfet=20
kgkonfet=0
print("1 килограмм конфет равен 20р")
dolar=koors
dolor=1
for i in range(1,100):
    dalar=dolar
    dolor+=1
    dolar+=koors
    print(dolor,"$","=",dolar,"р",kgkonfet,"Килограмм конфет")
    if dalar >= stoimostkgkonfet:
        kgkonfet+=1
        stoimostkgkonfet+=19

        

