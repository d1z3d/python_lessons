# Задание №2

# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».

# Для решения задачи создайте переменную и в неё положите слово с помощью input()

# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False
word = input("Введите слово из маленьких латинских букв: ").lower()
vowels = "aeiou"

vowel_count = sum(1 for letter in word if letter in vowels)
consonant_count = sum(1 for letter in word if letter.isalpha() and letter not in vowels)

print("False" if vowel_count == 0 else f"Количество гласных букв: {vowel_count}\nКоличество согласных букв: {consonant_count}")