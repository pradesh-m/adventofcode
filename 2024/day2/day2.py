PROBLEM_PATH = "inputdata/day4data.txt"

grid = []
with open(PROBLEM_PATH, 'r') as file:
    for line in file:
        row_str = line.strip()
        if row_str:
            grid.append(row_str)

n = len(grid)
m = len(grid[0]) if n > 0 else 0

count = 0

for row in range(1, n - 1):
    for col in range(1, m - 1):
        if grid[row][col] == 'A':
            diag1 = grid[row-1][col-1] + grid[row][col] + grid[row+1][col+1]
            diag2 = grid[row+1][col-1] + grid[row][col] + grid[row-1][col+1]

            if diag1 in ["MAS", "SAM"] and diag2 in ["MAS", "SAM"]:
                count += 1

print("count:", count)
