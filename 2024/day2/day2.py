TEST_PATH = "2024/day2/day2test.txt"
PROBLEM_PATH = "2024/day2/day2data.txt"

file_list = []

with open(PROBLEM_PATH, 'r',) as file:
    for line in file:
        int_line = [int(x) for x in line.strip().split()]
        file_list.append(int_line)

def invalid_report_indices(report):
    faulty_indices = []
    report_increasing = report[1] > report[0]
    for i in range(1, len(report)):
        if report[i] < report[i-1] and report_increasing == True or report[i] > report[i-1] and report_increasing == False:
            faulty_indices.append(i)
        elif not 1 <= abs(report[i-1]-report[i]) <= 3:
            faulty_indices.append(i)
    return faulty_indices

def invalid_indices(flist):
    result = []
    for report in flist:
        result.append(invalid_report_indices(report))
    return result
        
def remove_one(faulty_indices, report_index):
    for i in range(len(faulty_indices)):
        copied_list = file_list[report_index][:]
        copied_list.pop(faulty_indices[i])
        if len(invalid_report_indices(copied_list)) == 0:
            return True
    return False

invalid_indices_result = invalid_indices(file_list)   

result_p2 = 0
result_p1 = 0
for i, report in enumerate(invalid_indices_result):
    if not report:
        result_p1 += 1
        result_p2 += 1
    elif remove_one(report, i):
        result_p2 += 1

print("Part 1 Result:", result_p1)
print("Part 2 Result:", result_p2)