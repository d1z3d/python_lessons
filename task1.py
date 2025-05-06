# Задание №1

N = int(input("Введите количество чисел: "))

numbers = []
for number in range(N):
    number = int(input("Введите число: "))
    if number <= 1 or number >= 10000 or abs(number) > 1e5:
        print("Ошибка: число должно быть больше 1, меньше 10000 и по модулю не превышать 10^5")
        exit()
    
    numbers.append(number)

# Переворот массива
reversed_numbers = numbers[::-1]

# Вывод перевёрнутого массива
for number in reversed_numbers:
    print(number)
