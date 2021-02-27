stack=[]
stack2=[]
def spush():
    Spushi=int(input("Введите цифру которую нужно добавить в очередь:"))
    stack.append(Spushi)
    print(stack)
    stack.append(stack)
    stack.pop(stack)
    ochered=int(input("Продолжить очередь? да-1 нет-0"))
    if ochered==1:
        spush()
    else:
        print("Вся очередь",stack)
        print("Вышли из очереди",stack2)
spush()
