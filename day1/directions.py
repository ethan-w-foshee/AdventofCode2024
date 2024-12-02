# Get the list, and define some variables
master = open("./day1/master.txt", "r")
list1 = []
list2 = []
finalSum = 0

# I'm iterating through the master list and breaking it into two
for x in master:
    newNum = x[0:5]
    newNum2 = x[6:11]
    list1.append(int(newNum))
    list2.append(int(newNum2))

# Sort literally just sorts the numbers from least to greatest
list1.sort()
list2.sort()

# Compare them, and take the absolute value difference, then add it all together
for index, x in enumerate(list1):
    finalSum += abs(x - list2[index])

print(finalSum)
# I FIGURED OUT HOW TO COMMENT!
# Part 2 begins here
itDo = 0
finalSum2 = 0
for x in list1:
    itDo = 0
    for y in list2:
        if x == y:
            itDo += 1
    else:
        finalSum2 += itDo * x 

print(finalSum2)