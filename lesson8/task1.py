# Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит их к строке
# и отдает объединенными через разделитель delimiter
# Вызовите функцию, передав в нее два аргумента "Learn" и "python", 
# положите результат в переменную и выведите ее значение на экран
# Сделайте так, чтобы результирующая строка выводилась заглавными буквами




def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    resultik = f'{one}{delimiter}{two}'
    return resultik


resultik_resultika = get_summ('Learn', 'python')
print(resultik_resultika.upper())