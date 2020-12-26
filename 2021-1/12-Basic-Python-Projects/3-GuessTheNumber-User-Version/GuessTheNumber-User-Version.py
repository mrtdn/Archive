# Mert Dinçer

import random

print(f'Welcome to this easy game. Choose an interval. Computer will\n \
        try to guess it. If it is lower than its guess type "l" if not type "h".')
intv = input('Enter your interval as space-seperated: ')
interval = [int(i) for i in intv.split()]
x, y = interval[0], interval[1]


def make_computer_guess(x, y):
    count = 1
    number = int(input('Enter your number: '))
    comps_guess = random.randint(x, y)
    while comps_guess != number:
        print(f'Computer\'s guess: {comps_guess}')
        l_or_h = str(input('Lower or higher: '))
        if l_or_h == 'l':
            comps_guess = random.randint(x, comps_guess)
        elif l_or_h == 'h':
            comps_guess = random.randint(comps_guess, y)
        count += 1
    return count
 
 
print(f'Comp found it on {make_computer_guess(x, y)} try.')
