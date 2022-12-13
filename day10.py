from inputs import *

today = day10.strip()

today1 = """noop
addx 3
addx -5"""

today2 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

lines = today.splitlines()

cycle = 0
x = 1

cycleValue: dict[int:int] = {
	0:1
}

signalStrengthTotal = 0

def rotate(strg, n):

    return strg[n:] + strg[:n]

beginningRow = "###....................................."

text = ("_" * 40) * int(240/40)

print(text)

def runForCycles(cycleAmt, instr, arg = None):
	global cycle, x, signalStrengthTotal, text, beginningRow
	for i in range(cycleAmt):
		cycle += 1
		
		vis = list(text)
		temp = list(beginningRow)
		vis[cycle-1] = temp[(cycle-1) % 40]
		# print(vis[cycle-1])

		text = ''.join(vis)

		# print(cycle)
		# for i in range(0,len(text)+1,40):
		# 	# print(i-40,i)
		# 	print(text[i-40:i])

		# print(instr, cycle, x)
		if (cycle - 20) % 40 == 0:
			# print(cycle, x)
			signalStrengthTotal += (cycle * x)
		
		# if the amt of cycles is done
		if i == cycleAmt - 1:
			# perform action here
			if instr == "addx":
				x += arg
				# if cycle == 41:
				print(cycle, rotate(beginningRow, arg * -1), x)
				beginningRow = rotate(beginningRow, (arg * -1) % 40)
				# print("1234567890" * 4)
				# print(beginningRow, x)
			else:
				pass
			cycleValue[cycle] = x
		
		

for instruction in lines:
	instr = instruction.split(" ")[0]
	if instr == "addx":
		arg = int(instruction.split(" ")[1]) 
		runForCycles(2,instr,arg=arg)
	else:
		runForCycles(1,instr)

print(signalStrengthTotal, x)
for i in range(0,len(text)+1,40):
	# print(i-40,i)
	print(text[i-40:i])
