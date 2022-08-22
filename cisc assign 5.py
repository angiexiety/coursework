
# data = historical weather for the toronto btwn jan 1938- dec 2018
# searches and sorts chronologically, outputs min/max/median temp, rain, and snow, creates txt file for annual avg

def readData(filename):
    '''Reads the weather data from the supplied filename. The function returns a list of
dictionaries, where each dictionary consists of the data for a particular month.'''
    fileIn = open(filename, 'r')
    allData = []
    line = fileIn.readline()
    while line != "":
        line = fileIn.readline().strip()
        if line != "":
            values = line.split(',')
            monthData = {}
            monthData['year'] = int(values[0])  # Key names used in dictionary.
            monthData['month'] = int(values[1])
            monthData['meanT'] = float(values[2])
            monthData['maxT'] = float(values[3])
            monthData['minT'] = float(values[4])
            monthData['rain'] = float(values[5])
            monthData['snow'] = float(values[6])
            allData.append(monthData)
    fileIn.close()
    return allData


def showSome(allData):
    '''A convenience function that prints the beginning and end portions of the supplied list.'''
    for i in range(10):
        print(allData[i])
    print("<snip>")
    for i in range(-10, 0):
        print(allData[i])


def getInt(prompt, lowLimit=None, highLimit=None):
    '''A robust function that is sure to return an int value between the two
supplied limits.'''
    numberOK = False
    while not numberOK:
        try:
            userNum = int(input(prompt))
            if lowLimit != None and userNum < lowLimit:
                print("input must be higher than", lowLimit)
                print("try again.")
            elif highLimit != None and userNum > highLimit:
                print("input must be lower than", highLimit)
                print("try again.")
            else:
                numberOK = True
        except ValueError:
            print("your entry is not valid. enter an integer.")
    return userNum


def addYearMonthKey(allData):
    '''Calculates and adds a key:value pair to each dictionary in the supplied list.
The key will be named 'yearmonth' and will have a value of (100 * year + month).'''
    for monthData in allData:
        monthData['yearmonth'] = monthData['year'] * 100 + monthData['month']

# end of supplied functions

def insertionSort(allData, key):
    '''Sorts the supplied list of dictionaries in situ into increasing order
by the key name supplied.'''
    for i in range(1, len(allData)):
        value = allData[i]
        while i > 0 and allData[i - 1][key] > value[key]:
            allData[i] = allData[i - 1]
            i -= 1
        allData[i] = value


def findRain(allData, target):
    '''Uses a binary search to locate rainfall amounts in mm from the supplied list of
dictionaries.  target is a date in the 'yearmonth' value format.  The function assumes
that the list has been sorted by increasing date.  The function will raise a ValueError
exception if the year and month in target do not exist in allData.'''
    index = 0
    length = len(allData) - 1
    while not index > length:
        mid = int(index + length) // 2
        if allData[mid]["yearmonth"] < target:
            index = mid + 1
        elif allData[mid]["yearmonth"] > target:
            length = mid - 1
        else:
            return allData[mid]["rain"]
    raise ValueError("error: cannot find the target {0} in allData.".format(target))


def findMax(allData, key):
    '''Returns the record from allData that has the maximum value for the supplied key.'''
    maximum = allData[0]
    for i in range(1, len(allData)):
        if (allData[i][key] > maximum[key]):
            maximum = allData[i]
    return maximum


def findMin(allData, key):
    '''Returns the record from allData that has the minimum value for the supplied key.'''
    minimum = allData[0]
    for i in range(1, len(allData)):
        if (allData[i][key] < minimum[key]):
            minimum = allData[i]
    return minimum


def getAnnualSnow(allData):
    '''This function returns a list of dictionaries which consist of the total
snowfall for every year listed in allData.  Each record will consist of
{'year' : ####, 'totalsnow' : ###.#}, where # is a number.  There will be one record per year.
It does not matter if any month records are missing, the total snowfall is still calculated, by
assuminng zero snow for the missing months.'''
    minYear = int(allData[0]["year"])
    snow = [{"year": minYear, "totalsnow": 0}]
    for i in range(len(allData)):
        year = int(allData[i]["year"])
        snowIndex = year - minYear
        if len(snow) - 1 < snowIndex:
            snow.append({"year": year, "totalsnow": 0})
        snow[snowIndex]["totalsnow"] += float(allData[i]["snow"])
    return snow


def saveAnnualMeanTemp(allData, filename):
    '''This function calculates the mean temperatures for an entire year and saves this
data to the supplied file - one line in the file per year.
It is assumed that each year from 1938 to 2012 has 12 months.'''
    insertionSort(allData, 'yearmonth')

    minYear = int(allData[0]["year"])
    annualAverage = {minYear: 0}
    for i in range(len(allData)):
        year = int(allData[i]["year"])
        index = year - minYear
        lenMean = len(annualAverage) - 1
        if lenMean < index:
            annualAverage[year - 1] = annualAverage[year - 1] / 12
            annualAverage[year] = 0
        annualAverage[year] += float(allData[i]["meanT"])

    maxYear = int(allData[len(allData) - 1]["year"])
    annualAverage[maxYear] = annualAverage[maxYear] / 12

    try:
        fileOut = open(filename, "w")
        for key, value in annualAverage.items():
            fileOut.write(str(key) + " " + str(value) + "\n")
        fileOut.close()
    except OSError as message:
        print(message)


def main():
    # read the data file
    db = readData("TorontoWeatherData.csv")
    print("initial read from file:")
    showSome(db)
    addYearMonthKey(db)
    insertionSort(db, 'yearmonth')
    print("\nafter sorting by date:")
    showSome(db)

    # test binary search for rainfall amount given year and month.
    searchYear = getInt("enter year for rainfall search: ", 1938, 2018)
    searchMonth = getInt("enter month for rainfall search: ", 1, 12)
    searchYearMonth = 100 * searchYear + searchMonth
    try:
        rainfall = findRain(db, searchYearMonth)
        print("rainfall was {0} mm.".format(rainfall))
    except ValueError as message:
        print(message)

    # test the find max & min functions by locating extremes temp. return single dictionary
    maxR = findMax(db, 'maxT')
    print("\nhighest temperature {0} degree celcius , in month {1}, {2}.".format(maxR['maxT'], maxR['month'], maxR['year']))
    minR = findMin(db, 'minT')
    print("lowest temperature {0} degree celcius , in month {1}, {2}.".format(minR['minT'], minR['month'], minR['year']))
    maxR = findMax(db, 'rain')
    print("highest rainfall {0} mm, in month {1}, {2}.".format(maxR['rain'], maxR['month'], maxR['year']))
    maxR = findMax(db, 'snow')
    print("highest snowfall {0} cm, in month {1}, {2}.".format(maxR['snow'], maxR['month'], maxR['year']))

    # test the find max & min functions by locating extremes snowfall. return the list of dictionary
    annualSnow = getAnnualSnow(
        db)
    insertionSort(annualSnow, 'totalsnow')
    minR = annualSnow[0]
    print("\nlowest annual snowfall {0} cm, in {1}.".format(minR['totalsnow'], minR['year']))
    medR = annualSnow[len(annualSnow) // 2]
    print("median annual snowfall {0} cm.".format(medR['totalsnow']))
    maxR = annualSnow[len(annualSnow) - 1]
    print("highest annual snowfall {0} cm, in {1}.".format(maxR['totalsnow'], maxR['year']))

    # sort data by mean temp & obtain median
    insertionSort(db, 'meanT')
    minR = db[0]
    print("\nlowest mean temperature {0} degree celcius, in month {1}, {2}.".format(minR['meanT'], minR['month'], minR['year']))
    medR = db[len(db) // 2]
    print("mrdian mean temperature {0} degree celcius.".format(medR['meanT']))
    maxR = db[-1]
    print("highest mean temperature {0} degree celcius, in month {1}, {2}.".format(maxR['meanT'], maxR['month'], maxR['year']))

    # check for global worming
    saveAnnualMeanTemp(db, "YearMeans.txt")


main()