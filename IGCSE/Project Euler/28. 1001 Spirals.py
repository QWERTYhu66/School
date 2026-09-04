def spiral_diagonal_sum(n):
    total = 1
    number = 1
    for layer in range(1, (n // 2) + 1):
        step = 2 * layer
        for _ in range(4):
            number += step
            total += number
    return total

print(spiral_diagonal_sum(1001))
