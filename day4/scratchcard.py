import collections

cards = open("input.txt", 'r').readlines()

part1 = 0
for card in cards:
    start_index = card.find(':')
    end_index = card.find('|', start_index + 1)

    winning_numbers = card[start_index + 1:end_index].split()
    my_numbers = card[end_index+2: len(card)].split()
    # python list intersection to build an array of my winning numnbers per game
    my_winning_numbers = list(set(winning_numbers) & set(my_numbers))
    if len(my_winning_numbers) >=2:
        part1+=pow(2, len(my_winning_numbers)-1)
    else:
        part1+=len(my_winning_numbers)

print(f'PART ONE RESULT: {part1}')


part2=0
# defaultdict creates a default dict (duh) with the default value being a lambda function 
# this will create a dict containing all cards being {(Game)1:1, ...(Game)n:n}
card_to_count = collections.defaultdict(lambda: 1)
for idx, card in enumerate(cards):
    card_idx = idx+1
    card_to_count[card_idx]
    start_index = card.find(':')
    end_index = card.find('|', start_index + 1)
    winning_numbers = card[start_index + 1:end_index].split()
    my_numbers = card[end_index+2: len(card)].split()
    
    value = 0
    my_winning_numbers = list(set(winning_numbers) & set(my_numbers))
    for number in my_winning_numbers:
        # count my winning numbers inside of value
        value += 1
    # copy the winning card for the amount of winning numbers
    for i in range(value):
        card_to_count[card_idx+i+1] += card_to_count[card_idx]
print(f'PART TWO RESULT: {sum(card_to_count.values())}')