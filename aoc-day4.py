# there is full overlap in assignments when:
# if pair 1 start > pair 2 start and pair 1 end < pair 2 end
# OR if pair 2 start > pair 1 start and pair 2 end < pair 1 end

"""
# read in file
file1 = open("aoc-day4.txt", "r")

# loop through file, storing pair start/ends and comparing
fullOverlaps = 0

for line in file1:
    # parse through line to extract numbers
    line = line.strip()
    start1, end1, start2, end2 = "", "", "", ""
    for c in line:
        if c == "-":
            break
        start1 += c
    line = line.replace(start1 + "-", "", 1)
    for c in line:
        if c == ",":
            break
        end1 += c
    line = line.replace(end1 + ",", "", 1)
    for c in line:
        if c == "-":
            break
        start2 += c
    line = line.replace(start2 + "-", "", 1)
    end2 = line
    
    # done processing #s, now check for full overlap
    
    start1, end1 = int(start1), int(end1)
    start2, end2 = int(start2), int(end2)

    # if pair 1 fully contained in pair 2:
    if start1 >= start2 and end1 <= end2:
        fullOverlaps += 1
    elif start2 >= start1 and end2 <= end1:
        fullOverlaps += 1

file1.close()

print("The total number of full assignment overlaps is: " + str(fullOverlaps))

"""

# PART 2 -------------------------------------------------

# read in file
file1 = open("aoc-day4.txt", "r")

# loop through file, storing pair start/ends and comparing
overlaps = 0

for line in file1:
    # parse through line to extract numbers
    line = line.strip()
    start1, end1, start2, end2 = "", "", "", ""
    for c in line:
        if c == "-":
            break
        start1 += c
    line = line.replace(start1 + "-", "", 1)
    for c in line:
        if c == ",":
            break
        end1 += c
    line = line.replace(end1 + ",", "", 1)
    for c in line:
        if c == "-":
            break
        start2 += c
    line = line.replace(start2 + "-", "", 1)
    end2 = line
    
    # done processing #s, now check for any overlaps
    
    start1, end1 = int(start1), int(end1)
    start2, end2 = int(start2), int(end2)

    # if pair 1 overlaps w pair 2
    if start2 in range(start1, end1 + 1):
        overlaps += 1
    elif start1 in range(start2, end2 + 1):
        overlaps += 1

file1.close()

print("The total number of assignment overlaps is: " + str(overlaps))