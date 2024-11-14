# Задача "План перехват":
def personal_sum(numbers):
    result = 0 # сумма чисел
    incorrect_data = 0 # кол-во некорректных данных
    for n in numbers:
        try:
            result += n
        except TypeError:
            incorrect_data += 1
        print(f'Некорректный тип данных для подсчёта суммы {n}')
    return result, incorrect_data
def calculate_average(numbers):
    try:
        sum_result, incorrect_date = personal_sum(numbers) #  вызываем personal_sum для подсчета суммы и некорректрных данных
        return sum_result / (len(numbers) - incorrect_date) # вычисляем среднее арифметическое всех чисел
    except ZeroDivisionError:
        return 0
    except TypeError:
            print(f'В numbers записан некорректный тип данных')





print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
