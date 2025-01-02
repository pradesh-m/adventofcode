
count = 0 
file_list = []

with open('day2/day2data.txt', 'r',) as file:
    for line in file:
        int_line = [int(x) for x in line.strip().split()]
        file_list.append(int_line)

report_increasing = True
for report in file_list:
    
    valid_report = True
    
    report_increasing = report[1] > report[0]
   
    for i in range(1, len(report)):
        if report[i] < report[i-1] and report_increasing == True or report[i] > report[i-1] and report_increasing == False:
            valid_report = False
            break
        if not 1 <= abs(report[i-1]-report[i]) <= 3:
            valid_report = False
            break 
        
    if valid_report:
        count += 1
        
print(count)
                    

        
