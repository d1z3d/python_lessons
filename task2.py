# Homo habilis
# Homo erectus
# Homo neanderthalensis
# Homo floresiensis
# Homo naledi
# Homo heidelbergensis
# Homo luzonensis
# Homo sapiens

data = input("Введите все стадии развития человека через запятую: ")

# Разделяем строку на список
stages = [stage.strip() for stage in data.split(',')]

print(' => '.join(stages))