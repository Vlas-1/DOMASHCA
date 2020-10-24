Chislo=int(input("Введите число"))
for i in range(1,21):
    if Chislo==1:
        print("Нет")
    Chislo=Chislo/2
    print(Chislo)
    if Chislo>1.0:
        if Chislo<2.0:
            print("да")
            break
        else:
            print("нет")
            break
