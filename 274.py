#Задание 4

g = 11
for i in range(1, g, 2):
    i = ' ' * ((g - i) // 2) + '*' * i
    print(i)
for i in range(g, 0, -2):
    i = ' ' * ((g - i) // 2) + '*' * i
    print(i)