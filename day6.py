from inputs import *

today = day6.strip()

# lines = today.splitlines()

# today = "nppdvjthqldpwncqszvftbrmjlhg"

discoveredCharacters = []

counter = 1
for char in today:
	discoveredCharacters.append(char)
	if len(discoveredCharacters) > 14:
		discoveredCharacters = discoveredCharacters[1:]
		if len(discoveredCharacters) == len(set(discoveredCharacters)):
			break
			
	counter += 1

print(counter) 