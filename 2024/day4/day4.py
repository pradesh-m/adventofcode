TEST_PATH = "day4/day4test.txt"
PROBLEM_PATH = "inputdata/day4data.txt"

grid = []

with open(PROBLEM_PATH, 'r') as file:
    for line in file:
        grid.append(line.strip())

MAS_DIRS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

target = "MAS"

target_len = len(target)

def check_word(x, y, dx, dy, grid, target):
    for i in range(target_len):
        nx, ny = x + (i * dx), y + (i * dy)
        if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == target[i]):
            return False
    return True

ADJACENT_DIRS = [(2,0), (0,2), (-2,0), (0,-2)] 
# the directions that another diagonal MAS can be from the first MAS's M

def check_all_dirs(currI, currY, graph):
    for dx, dy in MAS_DIRS:
        if check_word(currI, currY, dx, dy, graph, target):
            return (True, (dx, dy))
    return False

visited = set() 

def adjacent_mas(firstmX, firstmY, graph, firstDir):
    firstDR = firstDir[0]
    firstDC = firstDir[1]
    # first: (0,0) going 1, 1 | second: (2,0) going -1, 1 or second: (0, 2) going 1, -1
    newCoords = [(2 * firstDR + firstmX, firstmY), (firstmX, 2*firstDC + firstmY)]
    for newx, newy in newCoords:
        if check_word(newx, newy, -firstDR, firstDC, graph, target) or check_word(newx, newy, firstDR, -firstDC, graph, target):
            A_pos = (firstmX + firstDR, firstmY + firstDC)
            if A_pos not in visited:
                visited.add(A_pos)
                return True
    return False

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == target[0]: 
            result = check_all_dirs(i, j, grid)
            if result:
                    if adjacent_mas(i, j, grid, result[1]): # if theres another MAS that makes an X
                        count += 1

print("count:", count)
