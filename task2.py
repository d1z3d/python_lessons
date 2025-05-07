# Задание №2

N = int(input("Введите количество чисел: "))
if N < 1 or N > 100000:
    print("Ошибка: N должно быть от 1 до 100000")
    exit()

numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(numbers)

if len(numbers) != N:
    print("Ошибка: количество чисел не соответствует N")
    exit()

for num in numbers:
    if num < 1 or num > 10**9:
        print("Ошибка: каждое число должно быть от 1 до 10^9")
        exit()

result = [numbers[-1]] + numbers[:-1]
print(*result)