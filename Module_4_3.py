from MyLib.sortfunc import *

data_1 = list(map(int, input("Введите числа через пробел").split()))
data_2 = list(map(int, input("Введите числа через пробел").split()))
data_3 = list(map(int, input("Введите числа через пробел").split()))

buble_sort(data_1)
insertion_sort(data_3)
selection_sort(data_2)

print(f'Пузырьковая сортировка: {data_1}')
print(f'Cортировка выбором: {data_2}')
print(f'Сортировка вставкой: {data_3}')
