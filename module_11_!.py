import pandas as pd

# Создание DataFrame из списка словарей
data = [{'name': 'Даниил', 'age': 22}, {'name': 'Иван', 'age': 24}]
df = pd.DataFrame(data)

print(df)
print()

# Фильтрация данных по условию
older_than_25 = df[df['age'] > 25]
print(older_than_25)
print()

# Группировка данных по столбцу
grouped_by_age = df.groupby('age')
print(grouped_by_age)
print()

# Сортировка данных по столбцам
sorted_df = df.sort_values(['age'], ascending=False)
print(sorted_df)
print()

# Агрегация данных
total_ages = df['age'].sum()
print(f"Сумма возрастов: {total_ages}")
print("\n Код pandas завершён \n")

#Основные функции Pandas:
#cоздание и работа с DataFrame — это основной объект в Pandas, который представляет собой двумерную структуру данных,
#похожую на таблицу в Excel;
#cериализация данных — возможность преобразования данных в различные форматы, такие как CSV, JSON, HTML и другие;
#манипуляция данными — возможность фильтрации, сортировки, группировки и агрегирования данных;
#анализ временных рядов — возможность работы с данными, которые изменяются со временем, такими как финансовые
#или метеорологические данные;
#визуализация данных — возможность создания графиков и диаграмм для наглядного представления данных.

import numpy as np

# Массивы:

# Создание одномерного массива целых чисел от 0 до 20
a = np.arange(21)
print(a)
print()

# Операции с массивами:

# Сложение двух массивов
a = np.arange(10)
b = np.ones(10) * 2
c = a + b
print(c)
print()

# Умножение массивов
d = np.arange(12).reshape(4, 3)
e = np.ones((4, 3))
f = d * e
print(f)
print("\n Код NumPy завершён \n")

#Основные возможности и функции библиотеки NumPy:

#NumPy - это мощный класс ndarray, который представляет собой многомерный массив чисел,
#символов или объектов. Массивы NumPy могут быть одномерными, двумерными, трехмерными и так далее;

#NumPy поддерживает широкий спектр операций с массивами, включая сложение, вычитание, умножение, деление,
#логические операции и т.д. Эти операции выполняются параллельно для всех элементов массива,
#что значительно ускоряет вычисления;

#NumPy предоставляет множество функций и методов для работы с массивами, включая линейную алгебру
#(например, умножение матриц), статистику (среднее значение, стандартное отклонение) и обработку изображений
#(преобразование Фурье)

import matplotlib.pyplot as plt

import numpy as np
# Работа с библиотекой matplotlib:

#Пример 1: Линейный график
#показывает как построить простой линейный график.

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 5, 6, 10, 12]

# Построение графика
plt.plot(x, y)

# Добавление заголовка и меток осей
plt.title("Линейный график")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Отображение графика
plt.show()

#Пример 2: Диаграмма рассеяния (Scatter Plot)
#Этот пример показывает, как создать диаграмму рассеяния, которая полезна
# для отображения зависимости между двумя переменными.



# Данные для диаграммы рассеяния
x = [5, 10, 8, 7, 2, 17, 14, 9, 4, 11]
y = [87, 86, 90, 72, 101, 82, 103, 87, 94, 78]

# Построение диаграммы рассеяния
plt.scatter(x, y, color='r')

# Добавление заголовка и меток осей
plt.title("Диаграмма рассеяния")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Отображение графика
plt.show()

# Пример 3: Гистограмма
# Этот пример показывает, как построить гистограмму для распределения случайных данных.

data = np.random.randn(1500)

# Построение гистограммы
plt.hist(data, bins=12, edgecolor='red')

# Добавление заголовка и меток осей
plt.title("Гистограмма")
plt.xlabel("Значения")
plt.ylabel("Частота")

# Отображение графика
plt.show()
