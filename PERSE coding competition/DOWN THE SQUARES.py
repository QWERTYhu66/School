num = int(input())
i = 1

while num > 0:
    num -= (i**2)
    i += 1

num += ((i - 1) ** 2)

print(num)