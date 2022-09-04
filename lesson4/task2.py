# Выведите на экран начальный элемент списка
# Выведите на экран последний элемент списка
# Напечатайте элементы списка со второго по четвертый включительно
# Удалите из списка строку "Python"

spichis = [3, True, 1000.3, 70, 'Python', '90']

print(spichis[0])
print(spichis[-1])
print(spichis[2:5])

spichis.remove('Python')
print(spichis)