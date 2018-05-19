
def valid(result):
    return result > 0 and result == round(result)

def foundInSets(result, sets):
    for oneSet in sets.values():
        if result in oneSet:
            return True
    return False

def addIfNeeded(result, sets, newSet):
    if(valid(result)):
        if(not foundInSets(result, sets)):
            newSet.add(result)

def processArgs(arg1, arg2, sets, newSet):
    addIfNeeded(arg1 + arg2, sets, newSet)
    addIfNeeded(arg1 - arg2, sets, newSet)
    addIfNeeded(arg2 - arg1, sets, newSet)
    addIfNeeded(arg1 * arg2, sets, newSet)
    addIfNeeded(arg1 / arg2, sets, newSet)
    addIfNeeded(arg2 / arg1, sets, newSet)

def deduce(sets, level):
    newSet = set()
    for level1 in range(1, level):
        level2 = level - level1

        for arg1 in sets[level1]:
            for arg2 in sets[level2]:
                processArgs(arg1, arg2, sets, newSet)
    sets[level] = newSet

sets = dict() # list of sets
sets[1] = { 6 }
for level in range(2, 8):
    deduce(sets, level)

print(sets)
print(foundInSets(100, sets))

