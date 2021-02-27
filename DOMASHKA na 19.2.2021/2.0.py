from math import sqrt
from random import randint
class descVector:
    x=2
    y=5
    z=10
    vectorx = x*x
    vectory = y*y
    vectorz = z*z
    def dVector(x,y,z): #Длина вектора
        xyz=sqrt(x * x + y * y + z * z)
        print("Длина вектора:",xyz)
    dVector(x,y,z)
    def scalVector(x,y,z,vectorx,vectory,vectorz): #Скалярное произведение
        scal=(x*vectorx +y*vectory+z*vectorz)
        print("Скалярное произведение:",scal)
    scalVector(x,y,z,vectorx,vectory,vectorz)
    def VVector(x,y,z,vectorx,vectory,vectorz): #Векторное произведение
        Vp=(y*vectorz-z*vectory,z*vectorx-x*vectorz,x*vectory-y*vectorx)
        print("Векторное произведение:",Vp)
    VVector(x,y,z,vectorx,vectory,vectorz)
    def ygolVector(scal): #угол между векторами
        Yv=(scal / xyz * xyz)
        print("угол между векторами:",Yv)
    def sumANDsum(x,y,z): #Сумма
        ss=(x+x*x+y*y+z+z*z)
        print("Сумма:",ss)
    sumANDsum(x,y,z)
    def razANDraz(x,y,z): #Разность
        ra=(x-x*x-y*y-z-z*z)
        print("Разность:",ra)
    razANDraz(x,y,z)
    def createVectors():
        N=int(input("Введите N, N сдесь x,y,z первого вектора:"))
        N1=int(input("Введите N, N сдесь x,y,z второго вектора:"))
        N2=int(input("Введите N, N сдесь x,y,z третьего вектора:"))
        x1=N
        y1=N
        z1=N
        x2=N1
        y2=N1
        z2=N1
        x3=N2
        y3=N2
        z3=N2
        vector1=round(sqrt(x1 * x1 + y1 * y1 + z1 * z1))
        vector2=round(sqrt(x2 * x2 + y2 * y2 + z2 * z2))
        vector3=round(sqrt(x3 * x3 + y3 * y3 + z3 * z3))
        print("Вектор 1 с размером:",vector1,"Вектор 2 с размером:",vector2,"Вектор 3 с размером:",vector3)
    createVectors()
        
        
