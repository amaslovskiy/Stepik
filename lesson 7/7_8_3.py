# Дано натуральное число , (n≤ 9). Напишите программу, которая печатает таблицу
# сложения для всех чисел от 1 до nn в соответствии с примером.

num = int(input())
for i in range(1, num + 1):
    for j in range(1, 10):
        for k in range(num):
            k = i + j
        print(i, '+', j, '=', k)
    print()
