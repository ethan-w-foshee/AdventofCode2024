master = open("./day2/master.txt", "r")
uppiesOrDownies = ""

def main():
    successes = 0
    for x in master:
        y = x.split(" ")
        if ascCheckTheThing(y):
            successes += 1
        elif dscCheckTheThing(y):
            successes += 1
    return successes

def ascCheckTheThing(arr):
    for index, z in enumerate(arr):
            z = int(z)
            if (index+1 < len(arr)):
                if int(arr[index + 1]) < z or (int(arr[index+1]) - z > 3) or (int(arr[index+1]) == z):
                    # print("[asc] HEY THIS ONE IS FALSE: ", arr)
                    return False
    else: 
        print("[asc] HEY THIS ONE IS TRUE: ", arr)
        return True

def dscCheckTheThing(arr):
    for index, z in enumerate(arr):
                z = int(z)
                if (index+1 < len(arr)):
                    if int(arr[index + 1]) > z or z - int(arr[index+1]) > 3 or (int(arr[index+1]) == z):
                        # print("[dsc] HEY THIS ONE IS FALSE: ", arr)
                        return False
    else:
        print("[dsc] HEY THIS ONE IS TRUE: ", arr)
        return True

print(main())