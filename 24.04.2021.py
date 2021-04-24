#1 - Основные задачи
 #0.1 - программа умеет делить, умножать, вычетать, плюсовать
 #0.2 - программа выполняется пока пользователь не введёт 0
 #0.3 - деление на ноль невозможно
stop=True
while stop==True: # начало цикла
    number1=int(float(input("Введите первое число:"))) # Первое число
    znak=input("Введите 0 для выхода или введите знак, примеры: / * - + 0:") # Знак
    number2=int(float(input("Введите второе число:"))) # Второе число
    if znak=="/": # Деление
        if number2==0: # Деление на ноль
            print("ДЕЛИТЬ НА НОЛЬ НЕЛЬЗЯ")
        else:
            otvet=number1/number2
            print("Ответ:", round(otvet)) # round здесь для того чтобы исключить .0 в ответе
    if znak=="*": # Умножение
        otvet=number1*number2
        print("Ответ:", otvet)
    if znak=="-": # Минус
        otvet=number1-number2
        print("Ответ:", otvet)
    if znak=="+": # Плюс
        otvet=number1+number2
        print("Ответ:", otvet)
    if znak=="0": # Выход из программы
        stop=False

