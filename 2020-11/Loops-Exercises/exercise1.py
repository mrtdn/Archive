# Abdullah Mert Dinçer
# b2200356016
# 22-November-2020

import sys

number = int(sys.argv[1])
power = int(sys.argv[2])
num = number ** power
sum = 0
counter = 0
print('Output :', str(number) + '^' + str(power), '=', end = ' ')
while True:
    if num >= 10:

        print(num, end = ' ')
        print('=', end=' ')
        for i in str(num):
            sum += int(i)
            counter += 1
            print(i, end = ' ')
            if counter < len(str(num)):
                print('+', end = ' ')
        print('=', end=' ')
        print(sum, end = '')
        counter = 0
        num = 0
        sum1 = sum
    elif sum >= 10:
        print(' =', end = ' ')
        sum = 0
        for i in str(sum1):
            sum += int(i)
            counter += 1
            print(i, end = ' ')
            if counter < len(str(sum1)):
                print('+', end = ' ')
        print('=', end = ' ')
        print(sum, end = '')
        if sum < 10:
            break
        sum1 = sum
        counter = 0
    else:
        break

print('')

