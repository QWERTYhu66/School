# First attempt:
# print((lambda n: f"Min: {min(n)}, Max: {max(n)}")([int(input(f"Enter number {i+1}: ")) for i in range(5)]))

# Second attempt:
print((lambda n: f"Min: {min(n)}, Max: {max(n)}")([int(input(f"Enter number {i+1}: ")) for i in range(int(input("How many numbers? ")))]))