"""
На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает
из указанных строк список и выводит его.
"""
s = []
number = int(input())
for i in range(number):
    s.append(input())
print(s)

"""
s = []
for _ in range(int(input)):
    s.append(input())
print(s)

"""
