# Задание №2

numbers1 = set(map(int, input("Введите числа первого списка через пробел: ").split()))
numbers2 = set(map(int, input("Введите числа второго списка через пробел: ").split()))
common_numbers = numbers1.intersection(numbers2)
print("Количество чисел, содержащихся в обоих списках:", len(common_numbers))