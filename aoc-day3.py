# ASCII code conversion to priorities:
# upper case range: 65-90
# A - ASCII 65, should be 27 --> subtract 38
# lower case range: 97-122
# a - ASCII 97, should be 1 --> subtract 96


def getPriority(c):
    """retrns the priority of a character c"""
    if (97 <= ord(c) and ord(c) <= 122):  # if lower case
        return ord(c) - 96
    if (65 <= ord(c) and ord(c) <= 90):  # if upper case
        return ord(c) - 38

"""
# read in file
file1 = open("aoc-day3.txt", "r")

sumPriors = 0

# loop through file, find common letters & sum priorities
for line in file1:
    comp1 = line[0:len(line)//2]
    comp2 = line[len(line)//2:]
    commonLetters = set(comp1).intersection(comp2)
    for s in commonLetters:
        sumPriors += getPriority(s)
        
file1.close()

print("The sum of the item priorities is: " + str(sumPriors))

"""

# PART 2 ----------------------------------------

# read in file
file1 = open("aoc-day3.txt", "r")

sumPriors = 0

# loop through file, find common letters & sum priorities
lines = file1.readlines()
for i in range(0, len(lines) - 2, 3):
    elf1 = lines[i].strip()
    elf2 = lines[i+1].strip()
    elf3 = lines[i+2].strip()
    badgeLetter = (set(elf1).intersection(elf2)).intersection(elf3)
    for s in badgeLetter:
        sumPriors += getPriority(s)
        
file1.close()
        
print("The sum of the badge priorities is: " + str(sumPriors))

    