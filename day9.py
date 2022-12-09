from inputs import *

today = day9.strip()

# today = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

# today = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""

lines = today.splitlines()

move = {
	"R":lambda x : (x[0] + 1, x[1]),
	"L":lambda x : (x[0] - 1, x[1]),
	"U":lambda x : (x[0], x[1] + 1),
	"D":lambda x : (x[0], x[1] - 1)
}



hPos = (0,0)
tPos = (0,0)

allTpositions = set()
def sign(x):
	return x / abs(x)

def separation(pos1, pos2):
	yDiff = pos1[1]-pos2[1]
	xDiff = pos1[0]-pos2[0]
	weirdDiff = yDiff * xDiff
	if yDiff == 0:
		weirdDiff = xDiff
	elif xDiff == 0:
		weirdDiff = yDiff

	# if sumDiff == 3:
		# move yPos diagonal 
	newX, newY = pos2[0], pos2[1]

	if weirdDiff > 1 or weirdDiff < -1:
		if xDiff != 0:
			newX += 1 * sign(xDiff)
		if yDiff != 0:
			newY += 1 * sign(yDiff)
	newPos = (newX, newY)
	return newPos

	# elif yDiff == 0:
	
	# elif xDiff == 0:

knotPos = {

}

n = 9

for i in range(n+1):
	knotPos[i] = (0,0)

for hMove in lines:
	dirH, amtH = hMove.split(" ")[0], int(hMove.split(" ")[1])

	for i in range(amtH):
		hPos = move[dirH](hPos)
		knotPos[0] = hPos

		for i in range(n):
			knotPos[i+1] = separation(knotPos[i], knotPos[i+1])
		allTpositions.add(knotPos[n])

print(len(allTpositions))