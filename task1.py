# Задание №1

def get_age_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return "года"
    else:
        return "лет"
    

pets = {}

name = input("Введите имя питомца: ")
animal_type = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

pets[name] = {
    "Вид питомца": animal_type,
    "Возраст питомца": age,
    "Имя владельца": owner_name
}

for key, value in pets.items():
    age_suffix = get_age_suffix(value["Возраст питомца"])
    print(f"Это {value['Вид питомца']} по кличке \"{key}\". Возраст питомца: {value['Возраст питомца']} {age_suffix}. Имя владельца: {value['Имя владельца']}")

