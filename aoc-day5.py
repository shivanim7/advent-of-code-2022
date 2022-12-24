from tqdm import tqdm
import sys

"""
starting stacks of crates

[N]     [C]                 [Q]    
[W]     [J] [L]             [J] [V]
[F]     [N] [D]     [L]     [S] [W]
[R] [S] [F] [G]     [R]     [V] [Z]
[Z] [G] [Q] [C]     [W] [C] [F] [G]
[S] [Q] [V] [P] [S] [F] [D] [R] [S]
[M] [P] [R] [Z] [P] [D] [N] [N] [M]
[D] [W] [W] [F] [T] [H] [Z] [W] [R]
 1   2   3   4   5   6   7   8   9 

"""
# create list of lists with the crates
crates = [["D", "M", "S", "Z", "R", "F", "W", "N"],  # stack 1
          ["W", "P", "Q", "G", "S"],                 # stack 2
          ["w", "R", "V", "Q", "F", "N", "J", "C"],  # stack 3
          ["F", "Z", "P", "C", "G", "D", "L"],       # stack 4
          ["T", "P", "S"],                           # stack 5
          ["H", "D", "F", "W", "R", "L"],            # stack 6
          ["Z", "N", "D", "C"],                      # stack 7
          ["W", "N", "R", "F", "V", "S", "J", "Q"],  # stack 8
          ["R", "M", "S", "G", "Z", "W", "V"]        # stack 9
          ]

# --------------------------------------------------------------------------------

mode = str(sys.argv[1])
# python aoc-day5.py [mode]


# PART 1 -------------------------------------------------------------------------

if mode == "1":
    # read file and loop through, executing the rearrangements
    file1 = open("aoc-day5.txt", "r")
    for line in tqdm(file1):
        line = line.split(" ")
        numCrates = int(line[1])
        startStack = int(line[3]) - 1
        endStack = int(line[5]) - 1
        
        # rearrange the crates according to this line's instruction
        for _ in range(numCrates):
            c = crates[startStack].pop()
            crates[endStack].append(c) 
                            
    file1.close()

    # find crate at top of each stack and add to string
    topCrates = ""
    for stack in crates:
        topCrates += stack[-1]

    print("The message containing crates at top of each stack is: " + topCrates)

# PART 2 -------------------------------------------------------------------------

else: # mode == "2"
    # read file and loop through, executing the rearrangements
    file1 = open("aoc-day5.txt", "r")
    for line in tqdm(file1):
        line = line.split(" ")
        numCrates = int(line[1])
        startStack = int(line[3]) - 1
        endStack = int(line[5]) - 1
        
        # rearrange the crates according to this line's instruction
        c = crates[startStack][-numCrates:]
        crates[endStack].extend(c)
        crates[startStack] = crates[startStack][:-numCrates]
            
    file1.close()

    # find crate at top of each stack and add to string
    topCrates = ""
    for stack in crates:
        topCrates += stack[-1]

    print("The message containing crates at top of each stack is: " + topCrates)   
