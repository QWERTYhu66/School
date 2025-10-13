# First attempt
print((lambda n: f"Min: {min(n)}, Max: {max(n)}")([int(input(f"Enter number {i+1}: ")) for i in range(5)]))

# Second attempt
print((lambda n: f"Min: {min(n)}, Max: {max(n)}")([int(input(f"Enter number {i+1}: ")) for i in range(int(input("How many numbers? ")))]))

# Bonus sort
def find_min_max(arr):
    return (min(arr), max(arr))

n = int(input("How many numbers? "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

min_val, max_val = find_min_max(numbers)

print(f"Min: {min_val}, Max: {max_val}")