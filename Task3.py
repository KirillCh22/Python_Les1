n =int(input("Введите количество чисел в последовательности: "))

count = 0

for i in range(n):
    user_num = int(input("Введите число: "))

    if user_num > 1:
        for div in range(2, user_num):
            if user_num % div == 0:
                break
        else:
            count += 1

print("Количество простых чисел = ", count)