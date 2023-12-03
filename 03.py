from tools import read
from operator import mul
from functools import reduce
import re

s = re.compile('[0-9]|\.')
n = re.compile('[0-9]+')
g = re.compile('\*')

data = read("03.txt")

w, h = len(data[0]), len(data)

symbol = [[not s.fullmatch(c) for c in line] for line in data]

def cover(j, s, e):
    ns = [(jj,ii) for jj in range(j-1, j+2) for ii in range(s-1,e+1)]
    return [(jj,ii) for (jj,ii) in ns if jj >= 0 and jj < h and ii >= 0 and ii < w]
    
def check_if_part_number(j, s, e):
    ns = cover(j,s,e)
    # print(ns)
    is_part_number = False
    for jj, ii in ns:
        is_part_number = is_part_number or symbol[jj][ii]
    return is_part_number

# a)

part_numbers = []
for j, line in zip(range(len(data)),data):
    for m in n.finditer(line):
        if check_if_part_number(j, m.start(), m.end()):
            part_numbers.append(int(m.group(0)))

print(sum(part_numbers))

# b)
    
number_table = [[-1 for c in line] for line in data]
numbers = []
k = 0
for j, line in zip(range(len(data)),data):
    for m in n.finditer(line):
        numbers.append(int(m.group(0)))
        for i in range(m.start(), m.end()):
            number_table[j][i] = k
        k = k + 1

def check_gear(j,i):
    ns = cover(j,i,i+1)
    num_indices = { number_table[x][y] for x,y in ns if number_table[x][y] != -1}
    if len(num_indices) == 2:
        return reduce(mul,[numbers[k] for k in num_indices], 1)
    return 0

total_gear_ratios = 0    
for j, line in zip(range(len(data)),data):
    for m in g.finditer(line):
        total_gear_ratios = total_gear_ratios + check_gear(j,m.start())

print(total_gear_ratios)