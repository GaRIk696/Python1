name = input("Ваше имя: ")
surname = input("Фамилия: ")
age = input("Возраст: ")

print("\nРеализация через метод format:")
output_1 = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(name, surname, age)
print(output_1)

print("\nРеализация через f-string:")
output_2 = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет"
print(output_2)