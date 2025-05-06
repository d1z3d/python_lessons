# Задание №3

data = input("Введите кол-во лодок").strip().split()
m = int(data[0])
n = int(data[1])
weights = list(map(int, data[2:2+n]))
    # сортируем по возрастанию
weights.sort()
i, j = 0, n - 1
boats = 0
while i <= j:
    if i < j and weights[i] + weights[j] <= m:
        i += 1
        j -= 1
    else:
        j -= 1
    boats += 1
print(boats)