from random import randint
EdinicaVesaA=10
EdinicaVesaJ=5
EdinicaVesaV=25
companyD=0
pogoda=(["Плохая","Хорошая"][randint(0,1)])
avariaV=1
avaria=randint(1,10)
avariaJ=randint(1,20)
avariaV=randint(1,50)
class Transport():
    def avariaa(companyD,plata): #Аварии Машин
        if avaria==1:
            print("О нет! Случилась авария.")
        else:
            companyD+=plata
            print("Перевозка прошла удачно, компания получила:",plata)
    def avariaaJ(companyD,plata): #Аварии на железных дорогах
        if avariaJ==1:
            print("О нет! Случилась авария.")
        else:
            companyD+=plata
            print("Перевозка прошла удачно, компания получила:",plata)
    def avariaaV(avariaV,companyD,plata): #Воздушные аварии 
        if avariaV==1:
            print("О нет! Случилась авария.")
        else:
            companyD+=plata
            print("Перевозка прошла удачно, компания получила:",plata)
    def VuborTransport(avariaV,avariaa): # Выбор транспорта
        print("Сегодня погода",pogoda)
        print("Компания заработала",companyD)
        print("Выберите тип транспорта для перевозки: Автомобильный, Железнодорожный, Воздушный")
        transport=str(input("Ваш ответ:"))
        if transport=="Автомобильный": # Автомобильный
            print("Выберите город: маленький (от 1 до 50 КМ), средний (от 51 до 100 КМ), большой (от 101 до 150 КМ)")
            gorod=str(input("Ваш ответ:"))
            if gorod=="маленький": # маленький АВТО
                print("Сколько КМ до города?:")
                km=int(input("Ваш ответ:"))
                if km<51:
                    print("На 1 км платится:",EdinicaVesaA)
                    plata=km*EdinicaVesaA
                    print("В итоге за перевозку вы получите:",plata)
                    avariaa(companyD,plata)
                if km>50:
                    print("Маленькие города не должны превышать 50 КМ")
            if gorod=="средний": # средний АВТО
                print("Сколько КМ до города?:")
                km=int(input("Ваш ответ:"))
                if km<51:
                    print("Слишком маленький маршрут для среднего города")
                if km<101:
                    print("На 1 км платится:",EdinicaVesaA)
                    plata=km*EdinicaVesaA
                    print("В итоге за перевозку вы получите:",plata)
                    avariaa(companyD,plata)
                if km>100:
                    print("Средние города не должны превышать 100 КМ")
            if gorod=="большой": # большой АВТО
                print("Сколько КМ до города?:")
                km=int(input("Ваш ответ:"))
                if km<101:
                    print("Слишком маленький маршрут для большого города")
                if km<151:
                    print("На 1 км платится:",EdinicaVesaJ)
                    plata=km*EdinicaVesaA
                    print("В итоге за перевозку вы получите:",plata)
                    avariaa(companyD,plata)
                if km>150:
                    print("большие города не должны превышать 100 КМ")
                    
        if transport=="Железнодорожный": # Железнодорожный
            print("Выберите город: средний (от 51 до 100 КМ), большой (от 101 до 150 КМ)")
            gorod=str(input("Ваш ответ:"))
            if gorod=="средний": # средний ЖЕЛЕЗ
                print("Сколько КМ до города?:")
                km=int(input("Ваш ответ:"))
                if km<51:
                    print("Слишком маленький маршрут для среднего города")
                if km<101:
                    print("На 1 км платится:",EdinicaVesaJ)
                    plata=km*EdinicaVesaJ
                    print("В итоге за перевозку вы получите:",plata)
                    avariaaJ(companyD,plata)
                if km>100:
                    print("Средние города не должны превышать 100 КМ")
            if gorod=="большой": # большой ЖЕЛЕЗ
                print("Сколько КМ до города?:")
                km=int(input("Ваш ответ:"))
                if km<101:
                    print("Слишком маленький маршрут для большого города")
                if km<151:
                    print("На 1 км платится:",EdinicaVesaJ)
                    plata=km*EdinicaVesaJ
                    print("В итоге за перевозку вы получите:",plata)
                    avariaaJ(companyD,plata)
                if km>150:
                    print("большие города не должны превышать 100 КМ")

        if transport=="Воздушный": # Воздушный
            print("Выберите город: большой (от 101 до 150 КМ)")
            gorod=str(input("Ваш ответ:"))
            if pogoda=="Плохая":
                print("Самолёт не может летать при полохой погоде")
            if gorod=="большой": # большой ВОЗД
                print("Сколько КМ до города?:")
                km=int(input("Ваш ответ:"))
                if km<101:
                    print("Слишком маленький маршрут для большого города")
                if km<151:
                    print("На 1 км платится:",EdinicaVesaV)
                    plata=km*EdinicaVesaV
                    print("В итоге за перевозку вы получите:",plata)
                    avariaaV(avariaV,companyD,plata)
                if km>150:
                    print("большие города не должны превышать 100 КМ")
    VuborTransport(avariaV,avariaa)
    

