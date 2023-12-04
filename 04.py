from tools import read
from operator import mul
from functools import reduce
import re

data = read("04.txt")

lp = re.compile('Card *([0-9]+):([0-9 ]*)\|([0-9 ]*)')

def parseline(line):
    m = lp.search(line)
    n = int(m.group(1))
    wins = { int(x) for x in m.group(2).split()}
    owns = { int(x) for x in m.group(3).split()}
    return n, wins, owns

def matches(wins, owns):
    return len([x for x in owns if x in wins])

def processline_a(line):
    n, wins, owns = parseline(line)
    ms = matches(wins, owns)
    if ms == 0:
        return 0
    return 2**(ms - 1)

def processline_b(line):
    n, wins, owns = parseline(line)
    return matches(wins, owns)

# a)

print(sum([processline_a(line) for line in data]))

# b)

l = len(data)
ncards_table = [0 for line in data]
for i in reversed(range(len(data))):
    copies = min(processline_b(data[i]), l - i - 1)
    ncards_table[i] = 1 + sum(ncards_table[i+1:i+copies+1])

print(sum(ncards_table))