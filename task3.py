# Задание №3

numbers = input("Введите последовательность чисел через пробел: ").split()
seen = set()
for number in numbers:
    if number in seen:
        print("YES")
    else:
        print("NO")
        seen.add(number)