while True:
    i = input("Введите число: ")
    if i.lower() == 'exit':
        print("Программа завершена.")
        break
    if i.lstrip('-').isdigit() and (i[0] != '-' or len(i) > 1):
        num_length = len(i.lstrip('-'))
        print(f"В этом числе {num_length} цифры.")
    else:
        print("Ошибка: данные не являются числом.")