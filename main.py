# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# some_list = list(map(int, input("Введите числа через пробел: ").split()))
# result = 0
# print(some_list)
# for i in range(len(some_list)):
#     if i % 2 == 1:
#         result = result + some_list[i]
# print("Сумма цифр на нечётных позициях =", result)

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# some_list = list(map(int, input("Введите числа через пробел: ").split()))
# result = []
#
# if len(some_list) % 2 > 0:
#     a = 1
# else:
#     a = 0
# for i in range(len(some_list)//2+a):
#     result.append(some_list[i]*some_list[-i-1])
# print(some_list)
# print(result)


# # Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части
# # 1.1 1.2 3.1 5 10.01
# def maximum(list):
#     max = list[0]
#     for i in list:
#         if i > max:
#             max = i
#     return max
# 
# 
# def minimum(list):
#     min = list[0]
#     for i in list:
#         if i < min:
#             min = i
#     return min
# 
# 
# some_list = list(map(float, input("Введите числа через пробел: ").split()))
# new_list = []
# for i in range(len(some_list)):
#     new_list.append(round(some_list[i] % 1, 2))
# for i in new_list:
#     if i == 0.0:
#         new_list.remove(0.0)
# # new_list.remove(0.0)
# min_num = minimum(new_list)
# max_num = maximum(new_list)
# print("Максимальное число дробной части =", max_num)
# print("Минимальное число дробной части =", min_num)
# print("Разница максимальной и минимальной дробной части =", max_num - min_num)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input("Введите число которое будет преобразовано в двоичную систему "))
final_list = []
none_list = []
count = 0
# while n//2 != 1 or 0:
#     final_list.append(n%2)
#     none_list.append(n//2)
#     n=n//2
#     print(n)
while n>1:
    final_list.append(n%2)
    none_list.append(n//2)
    n = n // 2
final_list.append(none_list[-1])
final_list.reverse()
print(none_list)
print(''.join(str(i)for i in final_list))