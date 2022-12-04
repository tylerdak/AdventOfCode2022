from inputs import day1

day1Input = day1.strip()

perElf = day1Input.split("\n\n")
allCaloricContent = []

for elf in perElf:
	items = elf.split("\n")
	totalThisElf = 0
	for item in items:
		totalThisElf += (int(item))
	allCaloricContent.append(totalThisElf)

allCaloricContent.sort()
allCaloricContent.reverse()
print("MOST TOTAL CALORIES: ", allCaloricContent[0])

print("SUM OF TOP 3: ", sum(allCaloricContent[:3]))
