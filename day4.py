from inputs import *

today = day4.strip()

eachpair = today.splitlines()

def rangeSubset(firstRange,secondRange):
    return firstRange.start in secondRange and firstRange[-1] in secondRange

def rangePart(firstRange,secondRange):
    return firstRange.start in secondRange or firstRange[-1] in secondRange

total = 0
parttotal = 0
for pair in eachpair:
    first, second = pair.split(',')[0],pair.split(',')[1]
    # print(first, )
    start1, end1 = first.split('-')[0],  first.split('-')[1]
    start2, end2 = second.split('-')[0],  second.split('-')[1]

    firstRange = range(int(start1), int(end1)+1)
    secondRange = range(int(start2), int(end2)+1)

    if rangeSubset(firstRange, secondRange) or rangeSubset(secondRange, firstRange):
        total += 1
    if rangePart(firstRange, secondRange) or rangePart(secondRange, firstRange):
        parttotal += 1
    if firstRange in secondRange:
        print(pair)
    if secondRange in firstRange:
        print(pair)

print(total)
print(parttotal)
