start = 1
finish = 101

count = 1

while True:
    n = (start + finish) // 2

    print("Загаданное число равно, меньше или больше:", n)

    answer = int(input("1 - равно, 2 - больше, 3 - меньше : "))

    if answer == 1:
        print("Угадали число с ", count, "попыток!")
        break
    elif answer == 2:
        start = n
    elif answer == 3:
        finish = n

    count += 1