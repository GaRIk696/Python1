input = input("Введите число: ")
# Проверяем, является ли введенное значение числом
if input.lstrip('-').isdigit():
    number = int(input)
    if number > 0:
        if number % 2 == 0:
            print(f"Число {number} является четным")
        else:
            print(f"Число {number} является нечетным")
    else:
        print("Ошибка: введено отрицательное число")
else:
    print("Ошибка: введено не число")