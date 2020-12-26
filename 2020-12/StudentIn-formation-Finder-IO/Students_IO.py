#Abdullah Mert Dinçer
# b2200356016
# 11-December-2020
import sys
f = open(sys.argv[1], 'r+')
lines = [line.rstrip('\n') for line in f.readlines()]
f.close()
splitLines = []
dict = {}
for i in lines:
    splitLines.append(i.split(':'))

for i in splitLines:
    for j in range(2):
        dict[i[0]] = i[1]
list2 = sys.argv[2].split(',')

for i in list2:
    try:
        print('Name: {0}, University: {1}'.format(i, dict[i]))
    except KeyError:
        print('No record of \'{0}\' was found.'.format(i))
