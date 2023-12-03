from collections import defaultdict
import re
from math import prod


# Determine which games would have been possible if the bag had been loaded 
# with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?

maxes = {
    "blue":14,
    "red":12,
    "green":13,
}

# load games
games = open("input.txt", 'r').readlines()

# Challenge One
count = 0
# iterate over games to analyze if they would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
for game in games:
    game = game.strip()
    id = game.split(": ")[0].split(" ")[-1]
    sets = [gs.strip().split(", ") for gs in (game.split(": ")[1]).split(";")]

    valid = True
    for se in sets:
        used = defaultdict(int)
        for val in se:
            tmp = val.split(" ")
            used[tmp[1]] = int(tmp[0])
        
        if used["blue"] > maxes["blue"] or used["red"] > maxes["red"] or used["green"] > maxes["green"]:
            # print(f'game #{id} is not valid')
            valid = False

    if valid:
        # print(f'game #{id} is valid')
        count += int(id)

print(f'Challenge One:', count)



# Challenge Two
power_tot = 0

def read_game(line):
    greens = re.findall(r"\d+\sgreen", line)
    greens = [int(green.split()[0]) for green in greens]

    blues = re.findall(r"\d+\sblue", line)
    blues = [int(blue.split()[0]) for blue in blues]

    reds = re.findall(r"\d+\sred", line)
    reds = [int(red.split()[0]) for red in reds]

    return { "greens": sum(greens), "blues": sum(blues), "reds": sum(reds) }

def read_line(line):

    min_green = 0
    min_blue = 0
    min_red = 0

    game_no = re.findall(r"\d+", line)[0]
    games = line.split(";")
    
    for game in games:
        game = read_game(game)
        game_red = game["reds"]
        game_greens = game["greens"]
        game_blues  = game["blues"]
        min_green = max(min_green, int(game_greens))
        min_blue = max(min_blue, int(game_blues))
        min_red = max(min_red, int(game_red))


    return prod([min_green, min_blue, min_red])

for line in games:
    line = line.strip()
    power_tot += read_line(line)


print(f'Challenge Two result is: {power_tot}')