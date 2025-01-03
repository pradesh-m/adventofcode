TEST_PATH = "day4test.txt"
PROBLEM_PATH = "day4data.txt"

grid = []
with open(PROBLEM_PATH, 'r',) as file:
    for line in file:
        curr_line = []
        for char in line:
            if char != "\n":
                curr_line.append(char)
        grid.append(curr_line)
    
print(grid)

def get_neighbors(currX, currY, grid):
    dirs = [
        (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = []
    for dx, dy in dirs:
        newX, newY = currX + dx, currY + dy
        if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]):
            neighbors.append((newX, newY))
    return neighbors
            
target = "XMAS"

def dfs(currX, currY, graph, target, index, visited):
    if index == len(target): 
        return 1

    visited.add((currX, currY))
    count = 0
    for neighborX, neighborY in get_neighbors(currX, currY, graph):
        if (neighborX, neighborY) not in visited and graph[neighborX][neighborY] == target[index]:
            count += dfs(neighborX, neighborY, graph, target, index + 1, visited)
    return count


result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == target[0]:
            result += dfs(i, j, grid, target, 1, set())

print(result)
    