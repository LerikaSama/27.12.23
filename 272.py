# задание 2

size = int(input("Введите размер клетки: "))
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("_" * size, end="")
        else:
            print("*" * size, end="")
    print()