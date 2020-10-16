for i in range(1,999):
    a=int(input("Введите цифру"))
    if a > -10 and a < 10:
        a += 5
    else:
        a -= 10
    print (a)
