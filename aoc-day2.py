# build a dictionary with the scores
# possible wins: P < S, S < R, R < P

scoreDict = {("A", "X") : 3,  # rock, rock
            ("A", "Y") : 6,   # rock, paper
            ("A", "Z") : 0,   # rock, scissors
            ("B", "X") : 0,   # paper, rock
            ("B", "Y") : 3,   # paper, paper
            ("B", "Z") : 6,   # paper, scissors
            ("C", "X") : 6,   # scissors, rock
            ("C", "Y") : 0,   # scissors, paper
            ("C", "Z") : 3,   # scissors, scissors
            
            "X" : 1,  # rock
            "Y" : 2,  # paper
            "Z" : 3  # scissors
          }

"""
# read in the file
file1 = open("aoc-day2.txt", "r")

# loop through the file and as we go, calculate scores
score = 0

for line in file1:
    opp = line[0]
    you = line[2]
    score += scoreDict[(opp, you)] + scoreDict[you]

print("Total score for strategy 1: " + str(score)) """


# PART 2 -----------------------------------------------------

moveDict = {("A", "X") : "Z",   # rock, lose --> play scissors
            ("A", "Y") : "X",   # rock, draw --> play rock
            ("A", "Z") : "Y",   # rock, win --> play paper
            ("B", "X") : "X",   # P, lose --> play R
            ("B", "Y") : "Y",   # P, draw --> play P
            ("B", "Z") : "Z",   # P, win --> play S
            ("C", "X") : "Y",   # S, lose --> play P
            ("C", "Y") : "Z",   # S, draw --> play S
            ("C", "Z") : "X",   # S, win --> play R
            
            "X" : 1,  # rock
            "Y" : 2,  # paper
            "Z" : 3  # scissors
          }

# read in the file
file1 = open("aoc-day2.txt", "r")

# loop through the file and as we go, find move then calculate score
score = 0
for line in file1:
    opp = line[0]
    outcome = line[2]
    yourMove = moveDict[(opp, outcome)]
    score += scoreDict[(opp, yourMove)] + scoreDict[yourMove]

print("Total score for strategy 2: " + str(score))