
# Task 1

user_height = int(input("Введите высоту рамки: "))
user_width = int(input("Введите ширину рамки: "))


print("\t\t\tРамка!\n")

for i in range(user_height + 1):
    for j in range(user_width + 1):
        if j == user_width or j == 0:
            print("|", end="")
        elif i == user_height or i == 0:
            print("-", end="")
        else:
            print(" ", end="")

    print()


print("\n\t\tРамка завершена!\n")






