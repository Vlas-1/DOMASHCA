c=1
print("Введите 0 чтобы идти вперёд")
print("Введите -1 чтобы повернуть на право")
print("Введите 1 чтобы повернуть на лево")
for i in range(1,900):
    a=int(input("Введите число"))
    if a==0:
        print("Вы сделали шаг вперёд")
    if a==1:
        c+=1
        print(c)
        if c==1:
            print("Робот смотрит на Север")
            print(c)
        if c==2:
            print("Робот смотрит на Запад")
        if c==3:
            print("Робот смотрит на Юг")
        if c==4:
            print("Робот смотрит на Восток")
        if c==5:
            c=1
            if c==1:
                print("Робот смотрит на Север")
                print(c)
    if a==-1:
        c+=-1
        if c==1:
            print("Робот смотрит на Север")
            print(c)
        if c==2:
            print("Робот смотрит на Запад")
        if c==3:
            print("Робот смотрит на Юг")
        if c==4:
            print("Робот смотрит на Восток")
        if c==0:
            c=4
            if c==4:
                print("Робот смотрит на Восток")
                print(c)






















