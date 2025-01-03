TEST_PATH = "2024/day4/day4test.txt"
PROBLEM_PATH = "2024/inputdata/day4data.txt"

grid = []

with open(PROBLEM_PATH, 'r') as file:
    for line in file:
        grid.append(line.strip())

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

target = "XMAS"
target_len = len(target)

def check_word(x, y, dx, dy, grid, target):
    for i in range(target_len):
        nx, ny = x + (i * dx), y + (i * dy)
        if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == target[i]):
            return False
    return True

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == target[0]: 
            for dx, dy in DIRS:
                if check_word(i, j, dx, dy, grid, target):
                    count += 1

print("count:", count)