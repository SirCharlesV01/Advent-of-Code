#total area of paper in square feet
paper_total = 0
#total length of ribbon in feet
ribbon_total = 0

with open("input.txt", "r") as dimensions:
    for line in dimensions:
        values = line.split("x")
        values = [ int(x) for x in values ]
        values.sort() #this guarantees the smalles area will be in areas[0].
        #get the areas of all faces of the prism
        areas = [2*values[0]*values[1], 2*values[0]*values[2], 2*values[2]*values[1]]
        #get the smalles perimeter around any one face of the prism:
        perimeter = 2*(values[0] + values[1])
        #get the volume of the present
        ribbon_length = perimeter + values[0]*values[1]*values[2]

        #update total values:
        ribbon_total += ribbon_length
        paper_total += sum(areas) + int(areas[0]/2)

print(paper_total)
print(ribbon_total)