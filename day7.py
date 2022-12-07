from inputs import *

today = day7.strip()

lines = today.splitlines()

filesystem: dict = {
	"/":{"subdirs":[],
	"files":[]}
}

def search(folder: str):
	data = filesystem[folder]
	files = data["files"]
	total = 0
	for file in files:
		size = file["size"]
		total += size

	subdirs = data["subdirs"]
	for dir in subdirs:
		total += search(dir)
	
	return total

pwd = "/"
for command in lines:
	parts = command.split(" ")
	type = parts[0]
	if type == "$":
		comm = parts[1]
		args = parts[2:]
		if comm == "cd":
			if args[0] == "/":
				pwd = "/"
			elif args[0] == "..":
				pwd = "/".join(pwd.split("/")[:-2]) + "/"
			else:
				pwd += args[0] + "/"
		elif comm == "ls":
			pass
	elif type == "dir":
		dirname = parts[1]
		# print("pwd, dirname:",pwd, dirname)
		fullDirPath = pwd + dirname + "/"
		filesystem[pwd]["subdirs"].append(fullDirPath)
		filesystem[fullDirPath] = {"subdirs":[],"files":[]}
	else:
		# this is a file
		size = int(parts[0])
		name = parts[1]

		# print(filesystem, pwd[:-1])
		filesystem[pwd]["files"].append({"size":size,"name":name})

total = 0



cap = 70000000
unusedGoal = 30000000

used = search("/")
unused = cap - used

currentSmallGuy = used
spaceToClear = unusedGoal - unused

for key in filesystem.keys():
	thisOne = search(key)
	if thisOne > spaceToClear and thisOne < currentSmallGuy:
		currentSmallGuy = thisOne
	if thisOne <= 100000:
		total += thisOne

print("Total for dirs under 100000:", total)
print(currentSmallGuy)
