
#Задание 1
start = input("Если вы хотите начать,введите: start ")

a = input(str("Введи число"))

print("Количество цифр")
print(len(str(a)))

b = 0
c = 1

for i in str(a):
 b += int(i)
c = b/len(str(a))

print("Среднее фрифметическое", c )

print("Количество нулей в этом числе",)
print(str(a).count("0"))
