from collections import defaultdict
import re
from math import prod
from functools import reduce

schematics = open("input.txt", 'r').read().strip().split('\n')
# print(schematics)

def find_number(x, line):
    # Check forward and backward on the line to find and return the full number
    number = [line[x]]
    for i in range(1, 3):  # Go max two before number
        if i >= 0 and line[x - i].isdigit():  # If the value is a number, add to front of list
            number.insert(0, line[x - i])
        else:
            break
    for i in range(1, 3):  # Go max two after number
        if i < len(line) and line[x + i].isdigit():  # If the value is a number, add to end of list
            number.append(line[x + i])
        else:
            break
    number = ''.join(number)  # Join list into a single number string
    print(number)
    return number

def check_around_symbol(x, y, data, part2=False):
    # Take coordinates of symbol and search around symbol for any digits
    surrounding_numbers = []
    for i in range(y - 1, y + 2):  # Should only check one above and one below
        if not i < 0 and not i >= len(data):
            prev_digit = False  # If the previous check was a number, this is True and ignore current number
            for j in range(x - 1, x + 2):  
                if not j < 0 and not j >= len(data[i]):
                    if data[i][j].isdigit() and not prev_digit:
                        surrounding_numbers.append(int(find_number(j, data[i])))
                        prev_digit = True
                    if not data[i][j].isdigit():  # Reset prev_digit when value is not a digit
                        prev_digit = False
    if part2:  # Part 2 almost reused code, but asked for multiplication instead if only 2 surrounding numbers
        if len(surrounding_numbers) == 2:
            return reduce(lambda x, y: x*y, surrounding_numbers)
        else: 
            return None
    else:
        return sum(surrounding_numbers)

def part1(parsed_data):
    pattern = re.compile(r'[^\w\s.]')
    total_value = 0
    for y, line in enumerate(schematics):
        for x, char in enumerate(line):
            if re.match(pattern, char):
                print(f"{char} is adjacent to:")
                total_value += check_around_symbol(x, y, parsed_data)  # Add total of surrounding values to total value

    print(total_value)


def part2(parsed_data):
    # On each line, if character is an asterisk, check surrounding values
    pattern = r'\*'
    total_value = 0
    for y, line in enumerate(parsed_data):
        for x, char in enumerate(line):
            if re.match(pattern, char):
                print("Gear is adjacent to:")
                gear_ratio =  check_around_symbol(x, y, parsed_data, True)
                if gear_ratio is not None:  # If a gear ration was returned, add to total value
                    print(f"Gear ratio is {gear_ratio}")
                    total_value += gear_ratio
                else:
                    print("No gear ratio")
    print(total_value)


part1(schematics)
part2(schematics)

