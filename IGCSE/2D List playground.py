grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = []
c = ""
for i in range(len(grid)):
    for a in range(len(grid[i])):
        b += str(grid[i][a])

for j in range(len(b) - 1):
    c += b[j] + ", "

c += b[-1]

print(c)