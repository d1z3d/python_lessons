# Задание №1

N = int(input("Введите количество чисел от 1 до 100000: "))

numbers = map(int, input("Введите числа через пробел: ").split())
if len(numbers) != N:
    print("Количество чисел не совпадает с введенным N.")
    exit()

unique_numbers = set(numbers)
print("Количество различных чисел:", len(unique_numbers))