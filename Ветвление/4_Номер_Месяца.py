# Напишите программу, которая получает номер месяца и выводит
# соответствующее ему время года или сообщение об ошибке.
                # Формат входных данных:
# Строка, содержащая номер месяца.
                # Формат выходных данных:
# Вывести соответствующее время года «Spring», «Summer», «Autumn» или
# «Winter», если такого номера месяца не существует вывести «Wrong number» .

seasons = { 'Winter' : (1, 2, 12),
            'Spring' : (3, 4, 5),
            'Summer' : (6, 7, 8),
            'Autumn' : (9, 10, 11)}

month = int(input())
if month > 0 and month < 13:
    for key in seasons.keys():
        if month in seasons[key]:
            print(key)
else:
    print('Wrong number')