from collections import defaultdict
TEST_PATH = "2024/day1/day1test.txt"
PROBLEM_PATH = "2024/day1/day1data.txt"

first = []
second = []
second_count = defaultdict(int)
difference = 0
similarity_score = 0


with open(TEST_PATH, 'r') as file:
    for line in file:
        line.strip()
        curr_line = line.split()
        first.append(int(curr_line[0]))
        second.append(int(curr_line[1]))
        second_count[int(curr_line[1])] += 1

first.sort()
second.sort()

for i in range(len(first)):
    difference += abs(first[i] - second[i])
    similarity_score += first[i]*second_count[first[i]]

print("difference: ", difference)
print("similarity score: ", similarity_score)
