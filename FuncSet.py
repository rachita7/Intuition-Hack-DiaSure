import random
import time
# -------------------------------------------------------------------------------
def randomize(value, accRange):  # to randomize the value of blood sugar within the accuracy range
    return random.uniform(value - accRange, value + accRange)
# -------------------------------------------------------------------------------
def sugarDiff(newMesSugar, oldMesSugar):  # finds drop in sugar level since last test
    return oldMesSugar - newMesSugar
# -------------------------------------------------------------------------------
def newInput(food_name, qty, bld_sgr, acc_r, overallDict, mealDict, bldSgrList, qtyList, accRangeList):
    i = len(overallDict)  # finds the next index number
    overallDict[food_name] = i  # indexDict must be the overall dictionary
    mealDict[food_name] = i
    bldSgrList.append(bld_sgr)
    qtyList.append(qty)
    accRangeList.append(acc_r)

# -------------------------------------------------------------------------------
def calcBefMeal(indexDictOfCurrMeal, bldSgrList, qtyList, accRangeList, measuredBldSgr):
    Sum = 0
    for key in indexDictOfCurrMeal:  # current meal dict is a new dict that is a subset of overall
        i = indexDictOfCurrMeal[key]
        val = randomize(bldSgrList[i], accRangeList[i])  # randomizes each value in the acc range
        netval = val * qtyList[i]
        Sum += netval
    sgrBefMeal = measuredBldSgr - Sum
    return sgrBefMeal
# -------------------------------------------------------------------------------
def updateAvgSlope(avgSlope, oldMesSgr, sgrBefMeal, timeSinceMeal, dayNum):
    new_slope = (oldMesSgr - sgrBefMeal) / timeSinceMeal
    avgSlope = (avgSlope * (dayNum - 1) + new_slope) / timeSinceMeal
    return avgSlope
# -------------------------------------------------------------------------------
def currBldSgr(avgSlope, timeSinceMeal, oldMesSgr):
    newSgr = oldMesSgr - avgSlope * timeSinceMeal
    return newSgr
# -------------------------------------------------------------------------------
def convertTime(time_str):  # Takes the time of meal in 24 hour format and converts to minutes
    hours = int(time_str[:2])
    minutes = int(time_str[2:])  # make sure that string length is 4 before using
    tot_mins = hours * 60 + minutes
    return tot_mins
# -------------------------------------------------------------------------------
def timeDiff(oldTime, newTime):  # using the minutes format above
    if newTime > oldTime:
        return newTime - oldTime
    else:
        return 24 * 60 + newTime - oldTime
# -------------------------------------------------------------------------------
def currentTime():  # returns the current time in minutes format
    t = [n for n in time.localtime(time.time())]
    hours = t[3]
    minutes = t[4]
    tot_mins = hours * 60 + minutes
    return tot_mins
# -------------------------------------------------------------------------------
def toDict(filename):
    f = open(filename, 'r')
    myDict = {}
    for line in f:
        k, v = line.strip().split(":")
        myDict[k.strip()] = int(v.strip())
    f.close()
    return myDict
# -------------------------------------------------------------------------------
def dictToFile(filename, myDict):
    f = open(filename, 'w+')
    for key in myDict:
        f.write("{Key}:{value}\n".format(Key=key, value=myDict[key]))
    f.close()
# -------------------------------------------------------------------------------
def listToFile(filename, myList):
    f = open(filename, 'w+')
    for item in myList:
        f.write("{i}\n".format(i=item))
    f.close()
# -------------------------------------------------------------------------------
def toList(filename):
    f = open(filename, 'r')
    iniList = f.readlines()
    finalList = [float(n) for n in iniList]
    return finalList
# -------------------------------------------------------------------------------
def readAll(overallDict, breakfastDict, lunchDict, dinnerDict, snacksDict, bldSgrList, qtyList, accRangeList, oldDetailsList):
    overallDict = toDict("overallDict.txt")
    breakfastDict = toDict("breakfast.txt")
    lunchDict = toDict('lunch.txt')
    dinnerDict = toDict('dinner.txt')
    snacksDict = toDict('snacks.txt')
    bldSgrList = toList('Blood_sugar.txt')
    qtyList = toList('qty.txt')
    accRangeList = toList('acc_range.txt')
    oldDetailsList = toList('details.txt')
# -------------------------------------------------------------------------------
def dictToList(myDict):
    myList = [n for n in myDict.keys()]
    return myList
# -------------------------------------------------------------------------------
def writeAll(overallDict, breakfastDict, lunchDict, dinnerDict, snacksDict, bldSgrList, qtyList, accRangeList, oldDetailsList):
    dictToFile("overallDict.txt", overallDict)
    dictToFile("breakfast.txt", breakfastDict)
    dictToFile('lunch.txt', lunchDict)
    dictToFile('dinner.txt', dinnerDict)
    dictToFile('snacks.txt', snacksDict)
    listToFile('Blood_sugar.txt', bldSgrList)
    listToFile('qty.txt', qtyList)
    listToFile('acc_range.txt', accRangeList)
    listToFile('details.txt', oldDetailsList)
# -------------------------------------------------------------------------------
def optimize(indexDictOfCurrMeal, bldSgrList, qtyList, accRangeList, measuredBldSgr, avgSlope, timeSinceMeal, oldMesSgr, sgrBefMeal):
    theoSgrBefMeal = oldMesSgr - avgSlope * timeSinceMeal
    sum_used =  oldMesSgr - sgrBefMeal
    diff = measuredBldSgr - (theoSgrBefMeal+sum_used)
    for key in indexDictOfCurrMeal:
        i=indexDictOfCurrMeal[key]
        if accRangeList[i]>abs(diff):
            accRangeList[i]=diff
        bldSgrList[i]+=diff/indexDictOfCurrMeal.len()
def no_of_lines():
    count = len(open().readlines())
    return count