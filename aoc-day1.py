       
# read in the file
file1 = open("aoc-day1.txt", "r")

# loop through the file and as we go,
# keep track of the max # of cals, the elf that carries it, and the number of elves

maxCals = 0
elvesCals = []
totalCals = 0

for line in file1: 
    if (len(s) > 0):
         totalCals += int(s)
    else:
        elvesCals.append(totalCals)
        # check if this elf has more cals than the current max
        print(totalCals)
        if totalCals > maxCals:
            maxCals = totalCals         
        totalCals = 0      

# close the file
file1.close()

# print the elf number carrying the max # of cals + how many cals it has
# print("The elf number carrying max # of cals is in position #: " + str(maxAt))
# print("Number of calories it is carrying: " + str(maxCals))

# find the top 3
max1 = max(elvesCals)
elvesCals.remove(max1)
max2 = max(elvesCals)
elvesCals.remove(max2)
max3 = max(elvesCals)

print("The total # of calories carried by top 3 elves is: " + str(max1 + max2 + max3))