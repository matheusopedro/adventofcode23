import re

lines = open("input.txt", 'r').readlines()
final_lst = []
for line in lines:
    # get numbers from line
    numbers = [c_val for c_val in [*line] if c_val.isdigit()]
    # print(numbers)

    if numbers[-1]:
        # Concatenate first and last digit in the string
        calibration_value = numbers[0]+numbers[-1]
    else:
        # Concatenate first and last digit in the string
        calibration_value = numbers[0]+numbers[0]
    
    final_lst.append(int(calibration_value))

print("final_lst, \n", final_lst)
print("final result")
# sum all calibration values retrieved from input
print(sum(final_lst))