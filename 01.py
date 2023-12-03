from tools import read
import re

a = re.compile('[0-9]')
b0 = re.compile('[0-9]|zero|one|two|three|four|five|six|seven|eight|nine')
b1 = re.compile('[0-9]|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|orez')
m = { str(i) : str(i) for i in range(10)} | {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

data = read("01.txt")

# a)

print( sum([int(a.search(l).group(0) + a.search(l[::-1]).group(0)) for l in data]))

# b)

print( sum([int(m[b0.search(l).group(0)] + m[b1.search(l[::-1]).group(0)[::-1]]) for l in data]))
