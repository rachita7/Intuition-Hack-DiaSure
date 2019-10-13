def recommend(currSgr, foodDict, osugl):
    diff= 160-currSgr
    mydictionary={}
    for key in foodDict:
        if(osugl[foodDict[key]]<=diff):
            qty= diff // osugl[foodDict[key]]
            mydictionary[key]=(osugl[foodDict[key]], qty)
    return mydictionary
#-------------------------------------------------------------------------------
def toDict(fileName):
    f = open(fileName, 'r')
    dict = {}
    for line in f:
         k, v = line.strip().split(':')
         dict[k.strip()] = int(v.strip())
    f.close()
    return dict
#-------------------------------------------------------------------------------
def exists(overallDict, item):
    for key in overallDict:
        if(overallDict[key]==item):
            return True
    return False
#-------------------------------------------------------------------------------
def getAllDicts(overallDict, breakfastDict, lunchDict, dinnerDict, snackDict):
    overallDict = toDict('overallDict.txt')
    breakfastDict = toDict('breakfast.txt')
    lunchDict = toDict('lunch.txt')
    dinnerDict = toDict('dinner.txt')
    snackDict = toDict('snack.txt')
#-------------------------------------------------------------------------------