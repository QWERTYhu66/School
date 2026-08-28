d1 = int(input())
d2 = int(input())
print_arr = ""


while d1 != d2:
    print_arr += str(d1)
    d1 += 1
    if d1 == 10:
        d1 = 0

print_arr += str(d1)

print(print_arr)