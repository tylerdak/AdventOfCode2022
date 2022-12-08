from inputs import *

today = day8.strip()

# today = """30373
# 25512
# 65332
# 33549
# 35390"""

lines = today.splitlines()

forest2D = []

for lineIndex, line in enumerate(lines):
	row = []
	for charIndex, char in enumerate(line):
		row.append(char)
	forest2D.append(row)



def visible(row, column):
	focus = forest2D[row][column] 
	numCol = len(forest2D[0])
	numRow = len(forest2D)

	visibleLeft = True
	visibleRight = True
	visibleUp = True
	visibleDown = True

	currCol = column
	currRow = row
	# left
	while currCol > 0:
		currCol -= 1
		currTree = forest2D[currRow][currCol]
		if int(currTree) >= int(focus):
			visibleLeft = False
			break
	currCol = column
	currRow = row

	# right
	while currCol < numCol-1:
		currCol += 1
		currTree = forest2D[currRow][currCol]
		if int(currTree) >= int(focus):
			visibleRight = False
			break

	currCol = column
	currRow = row
	# up
	while currRow > 0:
		currRow -= 1
		currTree = forest2D[currRow][currCol]
		if int(currTree) >= int(focus):
			visibleUp = False
			break
	currCol = column
	currRow = row
	# right
	while currRow < numRow-1:
		currRow += 1
		currTree = forest2D[currRow][currCol]
		if int(currTree) >= int(focus):
			visibleDown = False
			break

	return visibleDown  or visibleUp or visibleLeft or visibleRight

def scenic(row, column):
	focus = forest2D[row][column] 
	numCol = len(forest2D[0])
	numRow = len(forest2D)

	scoreLeft = 0
	scoreRight = 0
	scoreUp = 0
	scoreDown = 0

	currCol = column
	currRow = row
	# left
	while currCol > 0:
		currCol -= 1
		scoreLeft += 1
		currTree = forest2D[currRow][currCol]
		if int(currTree) >= int(focus):
			break
	currCol = column
	currRow = row

	# right
	while currCol < numCol-1:
		currCol += 1
		scoreRight += 1
		currTree = forest2D[currRow][currCol]
		if int(currTree) >= int(focus):
			break

	currCol = column
	currRow = row
	# up
	while currRow > 0:
		currRow -= 1
		scoreUp += 1
		currTree = forest2D[currRow][currCol]
		if int(currTree) >= int(focus):
			break
	currCol = column
	currRow = row
	# right
	while currRow < numRow-1:
		currRow += 1
		scoreDown += 1
		currTree = forest2D[currRow][currCol]
		if int(currTree) >= int(focus):
			break

	return scoreLeft * scoreRight * scoreUp * scoreDown

total = 0
scenicS = 0 

for i, row in enumerate(forest2D):
	for j, column in enumerate(row):
		if visible(i,j):
			total += 1
		thisScene = 0
		thisScene = scenic(row=i,column=j)
		if thisScene > scenicS:
			scenicS = thisScene

print(total, scenicS)