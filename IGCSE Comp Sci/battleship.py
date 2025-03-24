import random

rows, cols = 12, 12
letters = "ABCDEFGHIJKL"
grid = [["." for _ in range(cols)] for _ in range(rows)]

def place_ship(size=3):
    while True:
        o, r, c = random.choice(["H", "V"]), random.randint(0, rows-1), random.randint(0, cols-1)
        if o == "H" and c + size <= cols and all(grid[r][c+i] == "." for i in range(size)):
            for i in range(size): grid[r][c+i] = "B"; return
        if o == "V" and r + size <= rows and all(grid[r+i][c] == "." for i in range(size)):
            for i in range(size): grid[r+i][c] = "B"; return

def print_grid(reveal=False):
    print("\n   " + "  ".join(letters))
    for i, row in enumerate(grid, 1):
        print(f"{i:2} " + "  ".join(cell if reveal or cell != "B" else "." for cell in row))

def get_input():
    while True:
        try:
            t = input("\nEnter target (e.g., A5): ").upper()
            if t[0] in letters and 1 <= int(t[1:]) <= rows:
                return int(t[1:]) - 1, letters.index(t[0])
        except: pass
        print("Invalid input!")

place_ship()

while True:
    print_grid()
    r, c = get_input()
    if grid[r][c] == "B": grid[r][c] = "X"; print("\nHIT!")
    elif grid[r][c] == ".": grid[r][c] = "O"; print("\nMISS")
    else: print("\n🚢 Already tried!"); continue
    if not any("B" in row for row in grid): print("\nYOU WIN!"); print_grid(True); break
