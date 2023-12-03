import re
import wordtodigits

lines = open("input.txt", 'r').readlines()
# lines = open("input_s.txt", 'r').readlines()
final_lst = []

# challenge one
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


# challenge_two
pattern = r'one|two|three|four|five|six|seven|eight|nine|\d+'
num_string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit_dict = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9",
    }


def extract_number_from_string(x):  
        string_parts = re.findall(r"(?=(\d|" + "|".join(digit_dict) + r"))", x)
        print(string_parts)
        digits = [string_parts[0], string_parts[-1]]
        translated_digits = [d if d.isdigit() else digit_dict.get(d) for d in digits ]
        return int(''.join(translated_digits))

total = 0
for line in lines:
    total += extract_number_from_string(line)
    
print(total)