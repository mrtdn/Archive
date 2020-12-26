# Abdullah Mert Dinçer
# b2200356016
# 22-November-2020

import sys

stringnums = sys.argv[1]
number_list = stringnums.split(',')
int_list = []
counter = 0
counter2 = 0
counter3 = 0
a = 10
for i in number_list:
    counter += 1
    int_list.append(int(i))
for j in int_list:
    counter3 = 0
    for i in range(counter):
        if j == 1 and (2 * j - 1 + counter2) <= counter - counter2 - 1:
            int_list.pop(2 * j - 1 + counter2)
            counter2 += 1
        elif j != 1 and i != 0 and (j * i - 1 + counter3) <= counter - counter2 - 1:
            int_list.pop(j * i - 1 - counter3)
            counter2 += 1
            counter3 += 1
int_list.remove(2 * a - 1)
print('Output :', end = ' ')
for i in int_list:
    print(i, end = ' ')
print('')