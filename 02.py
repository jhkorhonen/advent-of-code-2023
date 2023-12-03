from tools import read
from operator import mul
from functools import reduce
import re

colours = { 'blue': 0, 'green': 1, 'red' : 2}


data = read("02.txt")

def parse_game(line):
    game, draws = line.split(':', 1)
    game_id = int(game[5:])
    
    draw_counts = [[], [], []]
    
    for draw in re.split('; |, ', draws):
        num, colour = draw.split(None,1)
        
        draw_counts[colours[colour]].append(int(num))
    
    return game_id, draw_counts

n_cols = 3
col_max = [14,13,12]

def is_valid(draws):
    valid = True
    for col in range(n_cols):
        if max(draws[col], default = 0) > col_max[col]:
            valid = False
    return valid

def minimum_sets(draws):
    return [ max(draws[col],default = 0) for col in range(n_cols)]

# a)

total = 0

for line in data:
    game_id, draws = parse_game(line)
    if is_valid(draws):
        total = total + game_id

print(total)

# b)

total = 0

for line in data:
    game_id, draws = parse_game(line)
    total = total + reduce(mul, minimum_sets(draws),1)
    
print(total)