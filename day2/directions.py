master = open("./day2/master.txt", "r")

# def main():
#     successes = 0
#     for x in master:
#         x = x.replace("\n", "")
#         y = x.split(" ")
#         if (checkAsc(y)):
#             successes += 1
#     return successes

# def checkAsc(arr):
#     arr2 = []
#     for x in arr:
#         arr2.append(int(x))
#     if arr2 == sorted(arr2) or arr2 == sorted(arr2, reverse=True):
#         return True
#     else:
#         return False

# def checkDupes(arr):
#     for index in range(len(arr)-1):
#         secondCheck = int(arr[index])
#         # print(secondCheck, arr[index])
#         if secondCheck == int(arr[index+1]):
#             return False
#         else:
#             return True
#     return False

# def checkDupeAgain(arr, num):
#     arr.pop(num)
#     for index in range(len(arr)-1):
#         thirdCheck = int(arr[index+1])
#         if thirdCheck == int(arr[index]):
#             # print("DUPE!!!!: ", thirdCheck, arr[index], " in ", arr)
#             return False
#     else:
#         # print("1 dupe, going to check diffs: ", arr, checkDiffs(arr))
#         return checkDiffs(arr)

# def checkDiffs(arr):
#     for index in range(len(arr)-1):
#         secondCheck = int(arr[index+1])
#         if abs(secondCheck - int(arr[index])) > 3:
#             # print("WRONG JUMP!!!!: ", secondCheck, arr[index])
#             return False
#     else:
#         return True

# print(main())

# ------------------
# Some random solution some guy put on the internet that I stole.
# Part 1 solution: 516
# Part 2 solution: 561

def check_sequence(seq):
    return (
        all(0 < seq[i+1] - seq[i] <= 3 for i in range(len(seq)-1)) or
        all(-3 <= seq[i+1] - seq[i] < 0 for i in range(len(seq)-1)))

with open('./day2/master.txt') as file:
    sequences = [list(map(int, line.strip().split())) for line in file]

num_valid = sum(check_sequence(seq) for seq in sequences)

num_valid_2 = sum( any(check_sequence(seq[:i] + seq[i+1:]) for i in range(len(seq)+1)) for seq in sequences)

print("Part 1:", num_valid)
print("Part 2:", num_valid_2)

