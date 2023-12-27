import random

lvl=int(input("Выберете уровень сложности, легко-1, средний-2, сложный-3:  "))
if lvl==1:
    ch=2
elif lvl==2:
    ch=5
else:
    ch=8

ball=5/ch
kol=0
while ch>0:
        i=random.randint(2,9)
        if lvl==1:
            i1=random.randint(2,3)
        elif lvl==2:
            i1=random.randint(2,6)
        else:
            i1=random.randint(2,9)
        ch=ch-1
        print(i,'x',i1)
        otv=int(input("Введите ответ: "))
        if otv==i*i1:
            print("Молодец!")
        kol=kol+ball
else:
    print("Неверно!")
    print("Ваша оценка ",kol)




