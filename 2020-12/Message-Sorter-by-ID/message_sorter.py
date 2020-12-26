# Abdullah Mert Dinçer - b2200356016
# 5-December-2020
import sys
file = open(f'{sys.argv[1]}', 'r+')
fileList = list(map(str, file.read().split('\n')))
file.close()
splitList = []
ultimateDict = {}
count = 0
counter = -1
for i in fileList:
    count += 1
    splitList.append(i.split('\t'))
splitList.sort()
for i in range(count):
    if splitList[i][0] in ultimateDict:
        ultimateDict[splitList[i][0]] += 1
    else:
        ultimateDict[splitList[i][0]] = 1
count = -1
messageCounter = 0
file = open(f'{sys.argv[2]}', 'w+')
for key in ultimateDict:
    messageCounter += 1
    file.write(f'Message {messageCounter}\n')
    for j in range(ultimateDict[key]):
        count += 1
        for m in range(3):
            file.write(splitList[count][m] + ' ')
        file.write('\n')
