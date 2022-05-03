"""
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу,
которая создает из указанных чисел список их кубов.
"""
s = []
num = int(input())
for i in range(num):
    s.append(int(input()) ** 3)
print(s)

# print([int(input()) ** 3 for i in range(int(input()))])

