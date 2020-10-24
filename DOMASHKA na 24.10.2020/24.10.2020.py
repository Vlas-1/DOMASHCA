dni=1
km=10
symKmDni=0
for i in range(1,31):
    print(dni,"день",km,"километров")
    km+=km/10
    symKmDni+=km
    dni+=1
    if dni==7:
        print("Лыжник прошол за 7 дней:",symKmDni,"км")
    if km>=80:
        print("Ему стоит остановится на",dni,"дне")
        print("Введите 0 если хотите завершить программу")
        userDay=int(input("Ведите день до которого лыжник будет тренироваться"))
        dni=0
        if userDay==0:
            break
        for i in range(1,userDay):
            print(dni,"день",km,"километров")
            km+=km/10
            dni+=1
    
