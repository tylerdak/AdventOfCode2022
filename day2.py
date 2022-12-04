from inputs import *

today = day2.strip()

eachturn = today.splitlines()

standardized = ["S","R","P"]

translations = {
	"A":"R",
	"B":"P",
	"C":"S",
	"X":"R",
	"Y":"P",
	"Z":"S"
}

winnings = {
	"R":"S",
	"P":"R",
	"S":"P"
}

howToWin = {
	"P":"S",
	"S":"R",
	"R":"P"
}

def scoreForPick(pick: str):
	match pick:
		case "X"|"R":
			return 1
		case "Y"|"P":
			return 2
		case "Z"|"S":
			return 3

def outcome(theirs: str, mine: str):
	theirsC, mineC = theirs, mine

	if theirs not in standardized:
		theirsC = translations[theirs]

	if mine not in standardized:
		mineC = translations[mine]

	if theirsC == mineC:
		return 3
	elif winnings[mineC] == theirsC:
		return 6
	else:
		return 0

def createOutcome(theirs: str, goal: str):
	theirsC = translations[theirs]
	if goal == "Y":
		return theirsC
	elif goal == "X":
		return winnings[theirsC]
	else:
		return howToWin[theirsC]

total = 0

newTotal = 0

for turn in eachturn:
	split = turn.split(" ")
	theirs, mine = split[0], split[1]

	total += scoreForPick(mine) + outcome(theirs,mine)

	myWin = howToWin[translations[theirs]]
	myPick = createOutcome(theirs, mine)
	newTotal += scoreForPick(myPick) + outcome(theirs,myPick)

print(total, newTotal)

