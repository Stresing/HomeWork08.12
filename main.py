def task1():
    # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции
    # Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

    some_list = list(map(int, input("Для заполнение списка, введите числа через пробел: ").split()))
    result = 0
    print("Созданный вами список ", some_list)
    for i in range(len(some_list)):
        if i % 2 == 1:
            result = result + some_list[i]
    print("Сумма цифр на нечётных позициях =", result)


def task2():
    # Напишите программу, которая найдёт произведение пар чисел списка.
    # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    # - [2, 3, 4, 5, 6] => [12, 15, 16];
    # - [2, 3, 5, 6] => [12, 15]

    some_list = list(map(int, input("Для заполнение списка, введите числа через пробел: ").split()))
    result = []

    if len(some_list) % 2 > 0:
        a = 1
    else:
        a = 0
    for i in range(len(some_list) // 2 + a):
        result.append(some_list[i] * some_list[-i - 1])
    print(some_list)
    print(result)


def task3():
    # Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части
    #  1.1 1.2 3.1 5 10.01 => 0.19

    def maximum(list):
        max = list[0]
        for i in list:
            if i > max:
                max = i
        return max

    def minimum(list):
        min = list[0]
        for i in list:
            if i < min:
                min = i
        return min

    some_list = list(map(float, input("Для заполнение списка, введите числа через пробел: ").split()))
    new_list = []
    for i in range(len(some_list)):
        new_list.append(round(some_list[i] % 1, 2))
    for i in new_list:
        if i == 0.0:
            new_list.remove(0.0)
    # new_list.remove(0.0)
    min_num = minimum(new_list)
    max_num = maximum(new_list)
    print("Максимальное число дробной части =", max_num)
    print("Минимальное число дробной части =", min_num)
    print("Разница максимальной и минимальной дробной части =", max_num - min_num)


def task4():
    # Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    # - 45 -> 101101
    # - 3 -> 11
    # - 2 -> 10

    n = int(input("Введите число которое будет преобразовано в двоичную систему: "))
    final_list = []
    none_list = []
    while n > 1:
        final_list.append(n % 2)
        none_list.append(n // 2)
        n = n // 2
    final_list.append(none_list[-1])
    final_list.reverse()
    print(''.join(str(i) for i in final_list))


def task5():
    # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    # для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
    def fib(n):
        if n in (1, 2):
            return 1
        return fib(n - 1) + fib(n - 2)

    def negfib(n):
        return (-1) ** (n + 1) * fib(n)

    amount = int(input("Введите число для проверки: "))
    some_list = [0]
    for i in range(1, amount + 1):
        some_list.append(fib(i))

    for i in range(1, amount + 1):
        some_list.insert(0, negfib(i))

    print(some_list)


task = int(input("Введите номер задания которое хотите проверить(1-5): "))
if task == 1:
    task1()
elif task == 2:
    task2()
elif task == 3:
    task3()
elif task == 4:
    task4()
elif task == 5:
    task5()
