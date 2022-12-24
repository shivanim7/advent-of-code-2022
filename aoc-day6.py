import sys

# choose to execute Part 1 or Part 2
mode = int(str(sys.argv[1]))
if mode == 1:
    size = 4
else: # mode == 2
    size = 14
    
# read file
file1 = open("aoc-day6.txt", "r")
line = file1.read()
file1.close()

charSet = set()
i = 3
while i < len(line) and len(charSet) < size:
    charSet = set()
    # add first 4 characters into the set
    for j in range(size):
        charSet.add(line[i-j])
    i += 1

print("The # of chars processed is: " + str(i))
    