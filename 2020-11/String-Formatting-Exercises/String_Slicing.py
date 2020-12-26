number = '9:254,487;978:548,487'
seperators = number[1::4]
values = ''.join(char if char not in seperators else ' ' for char in number).split()
print([int(val) for val in values])

abc = 'abcdefghijklmnopqrstuvwxyz'
print(abc[-10:13:-1])
print(abc[4::-1])
print(abc[:-9:-1])
print(abc[:-1])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"

values = ''.join(data[::5])
print([int(val) for val in values])

flower = 'blue violet'

print(abc[:-1])

day = 'Sunday'
temperature = -10
raining = False
if day == 'Sunday' and (temperature  >= 27 or raining == False):
    print('go swimming')


activity = input('What do you want to do today?\n')
if 'cinema' not in activity.casefold():
    print('I don\'t know man let\'s just go to cinema')
else:
    print('I thought so as well :)')


age = int(input('What\'s your age: '))
name = input('What\'s your name: ')
print(f'Hi there {name}!')
if 18 <= age < 31:
    print(f'Happy holidays {name}')
elif age < 18:
    print(f'Unfortunately you are not old enough. Please come back in {18 - age} years.')
else:
    print(f'Unfortunately you are not young enough. Please come back in your next life. :(')

