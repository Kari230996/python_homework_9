'''
📌 Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
'''
import math
import random
import csv
import json


def roots_of_quadratic_equation(a: int, b: int, c: int):

    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)

        return x1, x2

    elif D == 0:

        x = b / (2*a)
        return x

    elif D < 0:
        return None


def run_with_csv_data(func):
    def wrapper(file_name):
        with open(file_name, newline='') as file:

            csv_reader = csv.reader(file)

            for row in csv_reader:
                if len(row) == 3:
                    a, b, c = map(int, row)
                    result = func(a, b, c)
                    print(f'Для коэффициентов {a}, {b}, {c}:')

                    if result is not None:
                        if isinstance(result, tuple):
                            print(
                                f'Уравнение имеет два корня: {result[0]} и {result[1]}')
                        else:
                            print(f'Уравнение имеет один корень: {result}')
                    else:
                        print(
                            'Уравнение не имеет действительных корней. Корни будут комплексными числами.')
    return wrapper


@run_with_csv_data
def find_roots(a, b, c):
    return roots_of_quadratic_equation(a, b, c)


def generate_random_num(a, b):
    return random.randint(a, b)


def generate_random_row():
    return [generate_random_num(100, 999), generate_random_num(100, 999), generate_random_num(100, 999)]


def generate_csv_file(file_name, num_rows):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)

        for _ in range(num_rows):
            row = generate_random_row()
            writer.writerow(row)


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            data = {
                "parameters": {
                    "args": args,
                    "kwargs": kwargs
                },
                "result": result
            }

            with open(filename, "w") as json_file:
                json.dump(data, json_file, indent=4)

            return result
        return wrapper
    return decorator


@save_to_json('result.json')
def add(a, b):
    return a + b


# вывод квадратных уравнений
result = roots_of_quadratic_equation(1, 4, 4)

if result is not None:
    if isinstance(result, tuple):
        print(f'Уравнение имеет два корня: {result[0]} и {result[1]}')

    else:
        print(f'Уравнение имеет один корень: {result}')
else:
    print('Уравнение не имеет действительных корней. Корни будут комплексными числами.')


# вывод случайных чисел на каждой строке
file_name = 'random_numbers.csv'
num_rows = random.randint(100, 1000)

generate_csv_file(file_name, num_rows)

print(f"Сгенерирован файл {file_name} с {num_rows} строками.")


# Используем декорированную функцию для чтения данных из CSV-файла и нахождения корней
find_roots('random_numbers.csv')


# вывод функции с использованием декоратора json-файла
result = add(5, 3)
