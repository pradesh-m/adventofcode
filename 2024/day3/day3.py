TEST_PATH = "/Users/pradeshmainali/Desktop/advent of code/2024/day3/day3test.txt"
PROBLEM_PATH = "/Users/pradeshmainali/Desktop/advent of code/2024/day3/day3data.txt"


# mul(32, 32)

string = ""
with open(PROBLEM_PATH, 'r',) as file:
    for line in file:
        string += line


# PROB SHOULD CREATE A FUNCTION THAT CAN PARSE THROUGH AND CONSTRUCT FIRST AND SECOND STRING. WILL DO LATER.

# def construct_int(str, left_index):
#     integer = 0 
#     while (string[right_first_int]).isnumeric():
#         first_int += int("".join(string[right_first_int]))
#         right_first_int += 1

result = 0
enabled = True
for i, char in enumerate(string):
    if string[i:i+7] == "don't()": 
        enabled = False
    if string[i:i+4] == "do()":
        enabled = True
    
    if string[i:i+4] == "mul(" and enabled == True:
        left_first_int = i+4
        right_first_int = i+4 
        first_int = ""
        while (string[right_first_int]).isnumeric():
            first_int += ("".join(string[right_first_int]))
            right_first_int += 1
        if string[right_first_int] == "," and string[right_first_int+1].isnumeric():
            right_first_int += 1
            left_first_int = right_first_int
            second_int = ""
            while (string[right_first_int]).isnumeric():
                second_int += ("".join(string[right_first_int]))
                right_first_int += 1
            if string[right_first_int] != ")":
                continue
            else:
                result += int(first_int) * int(second_int)

                
            
        
    
    