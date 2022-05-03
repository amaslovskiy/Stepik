"""
На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу,
которая выводит k-ую букву из введенных строк на одной строке без пробелов.
"""
num = int(input())
s = [input() for _ in range(num)]
k = int(input())
for i in range(num):
    x = []
    x.extend(s[i])
    print(x[k - 1] if k <= len(x) else '', end='')

