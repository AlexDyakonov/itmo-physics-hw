import xlsxwriter
import random

class interval:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

workbook = xlsxwriter.Workbook('Labs\Lab1\\results.xlsx')
worksheet = workbook.add_worksheet()

N = 50

allNumbers = [4.89] * N

for i in range(N):
    allNumbers[i] = round(allNumbers[i] + random.random() * 0.21, 2)

allNumbers.sort()

for i in range(N):
    line1 = 'A' + str(i)
    worksheet.write(line1, i)
    line2 = 'B' + str(i)
    worksheet.write(line2, allNumbers[i])

min = min(allNumbers)
max = max(allNumbers)

numOfIntervals = 14
intervalsNotNormal = [0] * numOfIntervals


for i in range(numOfIntervals):
    if(i == 0):
        intervalsNotNormal[i] = min
    else:
        intervalsNotNormal[i] += round(intervalsNotNormal[i-1] + 0.05, 2) 

intervalsNotNormal.sort()

numOfIntervalPairs = 7
intervalsPairs = []*numOfIntervalPairs

for i in [0,2,4,6,8,10,12]:
    inter = interval(intervalsNotNormal[i], intervalsNotNormal[i+1]) 
    intervalsPairs.append(inter)
    

for i in range(numOfIntervals):
    line1 = 'F' + str(i + 5)
    worksheet.write(line1, intervalsNotNormal[i])
    
numbersBetweenIntervals = [0] * 7
    
def isInRange(btw : interval, num):
    if num > btw.x and num < btw.y:
        return True
    else: 
        return False

flag = 0

for i in range(numOfIntervalPairs):
    for j in range(N):
        if(isInRange(intervalsPairs[i], allNumbers[j]) == True):
            flag += 1
    numbersBetweenIntervals[i] = flag
    flag = 0

for i in range(numOfIntervalPairs):
    line1 = 'G' + str(i+5)
    worksheet.write(line1, numbersBetweenIntervals[i])


print(allNumbers)
print(numbersBetweenIntervals)

workbook.close()