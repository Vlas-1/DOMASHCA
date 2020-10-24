dni=1
km=10
symkmdni=0
for i in range(1,31):
    print(dni,"день",km,"километров")
    km+=km/10
    symkmdni+=km
    dni+=1
    if dni==7:
        print("Лыжник прошол за 7 дней:",symkmdni,"км")
    if km>=80:
        print("Ему стоит остановится на",dni,"дне")
        userday=int(input("Ведите день до которого лыжник будет тренироваться"))
        dni=0
        for i in range(1,userday):
            print(dni,"день",km,"километров")
            km+=km/10
            dni+=1
    
