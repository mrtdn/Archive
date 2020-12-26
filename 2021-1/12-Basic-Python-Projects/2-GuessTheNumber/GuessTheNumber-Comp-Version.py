# Mert Dinçer

import random


def guessthenumber(x):
    randomnumber = random.randint(1, 23)
    while x != randomnumber:
        x = int(input('Wrong! Try again: '))
    return 'Congratulations you got it correctly!'
print(guessthenumber(input('Enter a number: ')))
