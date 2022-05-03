"""
На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая
создает список из символов всех строк, а затем выводит его.
"""
s = []
[s.extend(input()) for _ in range(int(input()))]
print(s)

# s = []
# number = int(input())
# for i in range(number):
#     s.extend(input())
# print(s)
