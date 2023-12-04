"""
Day 4 :)
"""

# Part 2
scratch_cards = {}
def get_scratch_card_counts(game, i):
    winning_nums = game.split(':')[1].split('|')[0].split(' ')
    winning_nums = [num.strip() for num in winning_nums if num]
    my_nums = game.split(':')[1].split('|')[1].split(' ')
    my_nums = [num.strip() for num in my_nums if num]

    count = 0
    for num in my_nums:
        if num in winning_nums:
            count += 1
    
    scratch_cards[i] = count

# Part 1
def get_score(game):
    winning_nums = game.split(':')[1].split('|')[0].split(' ')
    winning_nums = [num.strip() for num in winning_nums if num]
    my_nums = game.split(':')[1].split('|')[1].split(' ')
    my_nums = [num.strip() for num in my_nums if num]
    score = 0
    for num in my_nums:
        if num in winning_nums:
            if score == 0:
                score = 1
            else:
                score = score * 2

    return score

with open('input.txt', 'r') as f:
    for i, game in enumerate(f.readlines()):
        get_scratch_card_counts(game, i + 1)

# Fill copies dict with winnings
count = 0
copies = {}
for k, val in scratch_cards.items():
    if k not in copies:
        copies[k] = {'games': [], 'counts': 1}
    
    for n in range(k+1, k + 1 + val):
        copies[k]['games'].append(n)

# Iterate the copies dict and propagate all the extra games
for k, val in copies.items():
    for g in val['games']:
        copies[g]['counts'] += val['counts']

# Count up all the games
running_count = 0
for val in copies.values():
    running_count += val['counts']

print(running_count)
