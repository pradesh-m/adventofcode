
TEST_PATH = "day7/day7test.txt"
PROBLEM_PATH = "inputdata/day7data.txt"

from collections import defaultdict

def build_data(path):
    data = defaultdict(set)
    with open(path, 'r') as file:
        for line in file:
            line = line.strip().split(':')
            line = "".join(line).split()
            for i in range(1,len(line)):
                data[int(line[0])].add(int(line[i]))

    return(data)

def main():
    data = build_data(TEST_PATH)
    print(data)


if __name__ == "__main__":
    main()