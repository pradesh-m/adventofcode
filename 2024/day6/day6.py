
TEST_PATH = "day6/day6test.txt"
PROBLEM_PATH = "inputdata/day6data.txt"

def build_data(path):
    with open(path, 'r') as file:
        grid = []
        obstructions = set()
        guard = []
        
        for i, line in enumerate(file):
            line.strip()
            curr_line = []
            for j, char in enumerate(line):
                if char != '\n':
                    curr_line.append(char)
                if char == '#':
                    obstructions.add((i,j))
                if char == '^' or char == '>' or char == '<' or char == 'v':
                    guard.append([i, j])
                    if char == '^': guard.append('^')
                    elif char == '>': guard.append('>')
                    elif char == '<': guard.append('<')
                    elif char == 'v': guard.append('v')
                        
            grid.append(curr_line)

    data = {'grid' : grid,
            'guard' : guard,
            'obstructions' : obstructions
            } 
    
    return data

def mark_path(data):
    grid = data['grid']
    curr_location = data['guard'][0]
    guard_facing = data['guard'][1]
    obstructions = data['obstructions']
    marked_path = set()
    
    face_to_dirs = {'^': [-1, 0],
                    '>': [0, 1],
                    '<': [0, -1],
                    'v': [1, 0]
        }
    
    transitions = {'^': '>',
                    '>': 'v',
                    'v': '<',
                    '<': '^'
        }
    while 0 <= curr_location[0] < len(grid) and 0 <= curr_location[1] < len(grid[0]):
        marked_path.add(tuple(curr_location))
        next_location = (curr_location[0]+face_to_dirs[guard_facing][0], curr_location[1]+face_to_dirs[guard_facing][1])
        if next_location in obstructions:
            guard_facing = transitions[guard_facing]
        else:
            curr_location = next_location

    return marked_path
        

def main():
    data = build_data(PROBLEM_PATH)
    marked_path = mark_path(data)
    print('Part 1:', len(marked_path))

if __name__ == "__main__":
    main()