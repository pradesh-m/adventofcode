TEST_PATH = "2024/day2/day2test.txt"
PROBLEM_PATH = "2024/day2/day2data.txt"

count = 0 
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
            continue
        if not 1 <= abs(report[i-1]-report[i]) <= 3:
            faulty_indices.append(i)
            continue 
    return faulty_indices

def invalid_indices(flist):
    result = []
    for report in flist:
        result.append(invalid_report_indices(report))
    return result
        
def remove_one(faulty_indices, report_index):
    if len(faulty_indices) > 1:
        return False
    
    attempt1 = file_list[report_index][:]
    attempt1.pop(faulty_indices[0])
    if len(invalid_report_indices(attempt1)) == 0:
        return True
    
    attempt2 = file_list[report_index][:]
    attempt2.pop(faulty_indices[0]+1)
    if len(invalid_report_indices(attempt2)) == 0:
        return True
    
    attempt3 = file_list[report_index][:]
    attempt3.pop(faulty_indices[0]-1)
    if len(invalid_report_indices(attempt3)) == 0:
        return True
    return False

invalid_indices_result = invalid_indices(file_list)   

safe_count = 0
for i, report in enumerate(invalid_indices_result):
    if not report:
        safe_count += 1
    elif remove_one(report, i):
        safe_count += 1
        print(safe_count)

print(safe_count)