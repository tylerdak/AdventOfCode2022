from inputs import *

today = day11.strip()

today1 = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

# lines = today1.splitlines()

rawMonkeys = today1.split("\n\n")

class Item:
    worryLevel: int

class Monkey:

    monkeyNum: int
    # itemsList: list[Item] = []
    denom: int
    trueMonkey: int
    falseMonkey: int
    # inspectTotal = 0

    def __init__(self) -> None:
        self.itemsList = []
        self.inspectTotal = 0
        self.op = lambda x: x



monkeys: dict[int,Monkey] = {}

for rawMonk in rawMonkeys:
    # print("THIS:",len(rawMonkeys))
    lines = rawMonk.splitlines()
    monkey = Monkey()
    for line in lines:
        line = line.strip()
        if line.startswith("Monkey"):
            monkey.monkeyNum = int(line.split(" ")[1][0])
        elif line.startswith("Starting"):
            itemsListStr: list[int] = line.split(":")[1].strip().split(",")
            for item in itemsListStr:
                newItem = Item()
                newItem.worryLevel = int(item)
                monkey.itemsList.append(newItem)
        elif line.startswith("Operation"):
            expression = line.split("new =")[1].strip()
            monkey.op = eval(f'lambda old: {expression}')
            if "old" not in expression:
                print("not trusting input... op = '0'")
                monkey.op = lambda x: x
        elif line.startswith("Test"):
            monkey.denom = int(line.split("divisible by")[1].strip())
        elif line.startswith("If true"):
            monkey.trueMonkey = int(line.split("throw to monkey")[1].strip())
        elif line.startswith("If false"):
            monkey.falseMonkey = int(line.split("throw to monkey")[1].strip())
    # print(len(monkey.itemsList))
    monkeys[monkey.monkeyNum] = monkey

rounds = 10000

for round in range(1,rounds+1):
    for key in sorted(monkeys.keys()):
        monkey = monkeys[key]
        toRemove = []
        for item in monkey.itemsList:
            # print(item.worryLevel)
            # print(len(monkey.itemsList), monkey.itemsList[9].worryLevel)
            # print(f"[Item {item.worryLevel}]: Begin")
            old = item.worryLevel
            new = monkey.op(old) # part 1
            # new = old # part 2 doesn't actually need worry levels
            # print(f"[Item {item.worryLevel}]: Calculated")

            monkey.inspectTotal += 1
            # print(monkey.monkeyNum)
            # print(old, monkey.op, new)

            # input()
            # item.worryLevel = int(new/3) # part 1 only
            item.worryLevel = new # part 2 only
            toRemove.append(item)
            # print(f"[Item {item.worryLevel}]: Queued to Remove")

            if item.worryLevel % monkey.denom == 0:
                monkeys[monkey.trueMonkey].itemsList.append(item)
            else:
                monkeys[monkey.falseMonkey].itemsList.append(item)
            # print(f"[Item {item.worryLevel}]: Passed Along")
        monkey.itemsList = []
    if round % 10 == 0:
        print("Reached round", round)

totaldMonkeys = {}

for monkey in monkeys.values():
    totaldMonkeys[monkey.monkeyNum] = monkey.inspectTotal

top = sorted(totaldMonkeys.values())
top.reverse()
answer = 1
for t in top[:2]:
    print("in t:",t)
    answer *= t

print(answer)





