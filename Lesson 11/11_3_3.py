"""
Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
"""

s = []
for i in range(26):
    s.append(chr(ord('a') + i) * (i + 1))
print(s)

# print([chr(97 + i) * (i + 1) for i in range(26)])
