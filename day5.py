import string
from inputs import *

exStack = """
[   [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3
 """

exMoves = """
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
 """

stacksViz = day5StackViz.strip()
inputStuff = day5.strip()
eachMove = inputStuff.splitlines()

#                     [Q]     [P] [P]
#                 [G] [V] [S] [Z] [F]
#             [W] [V] [F] [Z] [W] [Q]
#         [V] [T] [N] [J] [W] [B] [W]
#     [Z] [L] [V] [B] [C] [R] [N] [M]
# [C] [W] [R] [H] [H] [P] [T] [M] [B]
# [Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
# [B] [R] [B] [C] [D] [H] [D] [C] [N]
#  1   2   3   4   5   6   7   8   9 

stackLines = stacksViz.splitlines()
stacks: dict[int,list[str]] = {}

for line in stackLines:
    currCol = 1
    for charNum, char in enumerate(line, start=1):

        print(charNum, currCol, char)
        if char in ["[", "]", " "]:
            pass
        elif char in string.ascii_letters:
            currStack = stacks.get(currCol)
            stacks[currCol] = [char] if currStack is None else currStack + [char]
        if charNum % 4 == 2:
            currCol += 1
            # else:
                # print(char,charNum % 4)

print(stacks)

for move in eachMove:
    instructs = move.split(" ")
    amt, orig, new = int(instructs[1]), int(instructs[3]), int(instructs[5])

    origStack = stacks[orig]
    grabbed = origStack[:amt]
    updated = origStack[amt:]
    stacks[orig] = updated

    # only necessary for part 1, comment for part 2
    # grabbed.reverse() 

    stacks[new] = grabbed + stacks[new] 
    print(stacks)
goodKeys = sorted(stacks.keys())
for val in goodKeys:
    print(stacks[val][0], end="")