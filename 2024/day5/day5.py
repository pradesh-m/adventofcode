from collections import defaultdict

TEST_PATH = "day5/day5test.txt"
PROBLEM_PATH = "inputdata/day5data.txt"

def build_data(path):
    
    conditions = defaultdict(set) # maps x: a set of numbers, Y such that x must appear after all numbers in Y that occur in the line
    lines = []
    with open(path, 'r') as file:
        conds = True
        for line in file:
            
            if not conds:
                curr_line = (line.strip().split(','))
                curr_line = [int(x) for x in curr_line]
                lines.append(curr_line)
            else:
                nums = line.strip().split('|')
                if len(nums) > 1:
                    conditions[int(nums[1])].add(int(nums[0])) # num 0 must come before num 1 if num 0 exists in the line
                else:
                    conds = False # done with the conditions part of file
    return (conditions, lines)

def find_problematic_numbers(conditions, line):
    problematic_numers = set()
    nums_in_line = set(line)
    for i, num in enumerate((line)):
        nums_before_num = set(line[0:i])
        nums_must_appear_before = nums_in_line.intersection(conditions[num])
        if not nums_must_appear_before.issuperset(nums_before_num):
            problematic_numers = problematic_numers.union(nums_before_num.difference(nums_must_appear_before))
    return problematic_numers

def classify_lines(conditions, lines):
    valid_lines = []
    invalid_lines = []
    for line in lines:
        invalid_lines.append(line) if find_problematic_numbers(conditions, line) else valid_lines.append(line)
    return (valid_lines, invalid_lines)

def middle_values(lines):
    sum = 0
    for line in lines:
        sum += line[len(line)//2]
    return sum

def fix_invalid_lines(conditions, lines):
    fixed_lines = []
    for line in lines:
        curr_line = line
        nums_in_line = set(line)
        problematic_numbers = find_problematic_numbers(conditions, line)
        while problematic_numbers:
            curr = problematic_numbers.pop()
            prereqs = nums_in_line.intersection(conditions[curr])
            latest_prereq = max([line.index(x) for x in prereqs])
            curr_line.remove(curr)
            curr_line.insert(latest_prereq, curr)
            problematic_numbers = find_problematic_numbers(conditions, curr_line)
        fixed_lines.append(curr_line)
    return fixed_lines

def main():
    data = build_data(PROBLEM_PATH)
    conditions, all_lines = data[0], data[1]
    
    valid_lines, invalid_lines = classify_lines(conditions, all_lines)
    fixed_invalid_lines = fix_invalid_lines(conditions, invalid_lines)
    
    part_one_solution =  middle_values(valid_lines)
    part_two_solution = middle_values(fixed_invalid_lines)
    
    print('PART 1:', part_one_solution)
    print('PART 2:', part_two_solution)
    
if __name__ == "__main__":
    main()