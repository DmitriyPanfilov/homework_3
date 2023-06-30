# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

my_list = []
n = int(input('Введите количество элементов массива: '))
j = 0
resalt = 0
while n > j:
    my_list.append(int(input('введите масива: ' )))

    j += 1
x = int(input('Введите искомое число: '))

index_element = 0
min_element = my_list[0]

for i in range(1, n):
    buffer_element = my_list[i]
    if buffer_element < min_element:
        min_element = buffer_element
        index_element = i

print(f"Самый близкий по величине элемент к заданному числу {my_list[index_element]}")