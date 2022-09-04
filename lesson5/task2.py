# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением "27.05.2019"
# Выведите на экран длину словаря


slovarik = {"city": "Москва", "temperature": "20"}

print(slovarik.get('country', "Россия"))

slovarik['date'] = '27.05.2019'
print(len(slovarik))