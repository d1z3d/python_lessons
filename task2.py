# Задание №2

# Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый. Все числа каждого списка находятся на отдельной строке. Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.


def read_valid_numbers(prompt):
    while True:
        numbers = list(map(int, input(prompt).split()))
        if len(numbers) > 100000:
            print("Слишком много чисел. Введите не более 100000.")
        else:
            return set(numbers)

numbers1 = read_valid_numbers("Введите числа первого списка через пробел: ")
numbers2 = read_valid_numbers("Введите числа второго списка через пробел: ")
common_numbers = numbers1.intersection(numbers2)
print("Количество чисел, содержащихся в обоих списках:", len(common_numbers))