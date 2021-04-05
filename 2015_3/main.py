santa_row = 0
santa_col = 0

robo_row = 0
robo_col = 0


#we will use a 2d array to store the adress of visited houses [[santa_row0,santa_col0],[santa_row1,santa_col1]...[santa_rown,santa_coln]]
santa_houses = [[santa_row, santa_col]] #first house gets a present from santa
robo_houses = [[santa_row, santa_col]] #and also from robo-santa

f = open("input.txt", "r")
directions = f.readline()

# First part:
for char in directions:

    if char == "^":
        santa_row += 1
    elif char == "v":
        santa_row -= 1
    elif char == ">":
        santa_col += 1
    else:
        santa_col -= 1

    if [santa_row, santa_col] not in santa_houses:
        santa_houses.append([santa_row,santa_col])


print("During the first year, Santa visited: " + str(len(santa_houses)) + " houses." )

#Second part:
santa_row = 0
santa_col = 0

santa_houses = [[santa_row, santa_col]] #first house gets a present from santa
robo_houses = [[robo_row, robo_col]] #and also from robo-santa

Santas_turn = True

for i in range(len(directions)):
    if Santas_turn: # in case its santas turn
        Santas_turn = False
        if directions[i] == "^":
            santa_row += 1
        elif directions[i] == "v":
            santa_row -= 1
        elif directions[i] == ">":
            santa_col += 1
        else:
            santa_col -= 1

        if [santa_row, santa_col] not in santa_houses and [santa_row, santa_col] not in robo_houses: #we want to count houses who havent been visited by either santa o robo-santa
            santa_houses.append([santa_row,santa_col])

    else: #in case its robo-santas turn
        Santas_turn = True
        if directions[i] == "^":
            robo_row += 1
        elif directions[i] == "v":
            robo_row -= 1
        elif directions[i] == ">":
            robo_col += 1
        else:
            robo_col -= 1

        if [robo_row, robo_col] not in santa_houses and [robo_row, robo_col] not in robo_houses:
            robo_houses.append([robo_row,robo_col])



print("\nDuring the second year,\nSanta visited: " + str(len(santa_houses)) + " new houses.\nRobo-santa visited: " + str(len(robo_houses)) + " new houses.")
print("The total of houses to recieve at least one present is: " + str(len(santa_houses) + len(robo_houses) - 1)) #we count the first house only once, hence we substract 1