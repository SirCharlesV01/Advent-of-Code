
#begin in ground floor
floor = 0

#stores the position of the character which makes santa go in the basement for the first time (floor = -1)
first_bsmnt = 0

f = open("input.txt", "r")
input = f.readline()

for i in range(len(input)):
    if input[i] == ')':
        floor -= 1
    else:
        floor += 1

    if floor == -1 and first_bsmnt == 0:
        first_bsmnt = i+1


print(floor)
print(first_bsmnt)