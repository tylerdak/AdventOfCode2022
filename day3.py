from inputs import *

example = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

today = day3.strip()

rucksacks = today.splitlines()



# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def charToScore(char:str):
	if char.islower():
		return ord(char) - 96
	elif char.isupper():
		return ord(char) - 64 + 26

	else:
		print("uh oh")

total = 0

for ruck in rucksacks:
	comp1 = ruck[:int(len(ruck)/2)]
	# may be wrong
	comp2 = ruck[int(len(ruck)/2):]

	inter = (intersection(list(comp1),list(comp2)))

	if len(inter) == 1:
		total += charToScore(inter[0])
	else:
		print(inter)
		total += charToScore(inter[0])

print(total)

lastThree = []
newTotal = 0

for ruck in rucksacks:
	if len(lastThree) < 3:
		lastThree.append(ruck)
	if len(lastThree) == 3:
		inter1 = intersection(lastThree[0],lastThree[1])
		print(inter1)
		inter = intersection(inter1,lastThree[2])
		print(inter)
		score = charToScore(inter[0])
		newTotal += score
		lastThree = []

print(newTotal)



