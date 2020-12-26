"""
Abdullah Mert Dinçer
b2200356016
11 - December - 2020
Chess Game - Assignment 3
"""
import sys
f = open(sys.argv[1], 'r+')
commands = [line.rstrip('\n').split() for line in f.readlines()]
f.close()
"""------------------------------------------------------------------------------------------
I initialized game board and positions according to chess rules. And reversed the list to match up
the classical chess board.
"""
positions = {'r1': 'a1', 'n1': 'b1', 'b1': 'c1', 'qu': 'd1', 'ki': 'e1', 'b2': 'f1', 'n2': 'g1', 'r2': 'h1',
             'p1': 'a2', 'p2': 'b2', 'p3': 'c2', 'p4': 'd2', 'p5': 'e2', 'p6': 'f2', 'p7': 'g2', 'p8': 'h2',
             'R1': 'a8', 'N1': 'b8', 'B1': 'c8', 'QU': 'd8', 'KI': 'e8', 'B2': 'f8', 'N2': 'g8', 'R2': 'h8',
             'P1': 'a7', 'P2': 'b7', 'P3': 'c7', 'P4': 'd7', 'P5': 'e7', 'P6': 'f7', 'P7': 'g7', 'P8': 'h7'}
gameboard = [['R1', 'N1', 'B1', 'QU', 'KI', 'B2', 'N2', 'R2'],
             ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],
             ['r1', 'n1', 'b1', 'qu', 'ki', 'b2', 'n2', 'r2']]
gameboard.reverse()
index_to_letter = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h"}
letter_to_index = {
   "a": 0,
   "b": 1,
   "c": 2,
   "d": 3,
   "e": 4,
   "f": 5,
   "g": 6,
   "h": 7}
"""------------------------------------------------------------------------------------------
A function that returns the possible moves for white and black pawns.
"""
def pawnPossibles(parameter1, positions, gameboard):
    column, row = list(positions[parameter1].strip().lower())
    row = int(row) - 1
    column = letter_to_index[column]
    tempPossibleMoves = []
    if 'p' in parameter1:
        try:
            temp = gameboard[row+1][column]
            if (parameter1.isupper() is gameboard[row+1][column].isupper()) and gameboard[row + 1][column] != '  ':
                pass
            else:
                tempPossibleMoves.append([row+1, column])
        except:
            pass
    elif 'P' in parameter1:
        try:
            temp = gameboard[row-1]
            if (parameter1.isupper()) is (gameboard[row-1][column].isupper()) and gameboard[row - 1][column] != '  ':
                pass
            else:
                tempPossibleMoves.append([row-1, column])
        except:
            pass
    # With temp variable I filtered all negative values.
    temp = [i for i in tempPossibleMoves if i[0] >= 0 and i[1] >= 0]
    possibleMoves = ["".join([index_to_letter[i[1]], str(i[0] + 1)]) for i in temp]
    possibleMoves.sort()
    return possibleMoves
"""------------------------------------------------------------------------------------------
A function that returns possible moves for black and white knights for a given position.
"""
def knightPossibles(parameter1, positions, gameboard):
    column, row = list(positions[parameter1].strip().lower())
    row = int(row) - 1
    column = letter_to_index[column]
    tempPossibleMoves = []
    try:
        temp = gameboard[row + 1][column - 2]
        if (parameter1.isupper() is gameboard[row+1][column-2].isupper()) and gameboard[row + 1][column - 2] != '  ':
            pass
        else:
            tempPossibleMoves.append([row + 1, column - 2])
    except:
        pass
    try:
        temp = gameboard[row + 2][column - 1]
        if (parameter1.isupper() is gameboard[row+2][column-1].isupper()) and gameboard[row + 2][column - 1] != '  ':
            pass
        else:
            tempPossibleMoves.append([row + 2, column - 1])
    except:
        pass
    try:
        temp = gameboard[row + 2][column + 1]
        if (parameter1.isupper() is gameboard[row+2][column+1].isupper()) and gameboard[row + 2][column + 1] != '  ':
            pass
        else:
            tempPossibleMoves.append([row + 2, column+1])
    except:
        pass
    try:
        temp = gameboard[row + 1][column + 2]
        if (parameter1.isupper() is gameboard[row+1][column+2].isupper()) and gameboard[row + 1][column + 2] != '  ':
            pass
        else:
            tempPossibleMoves.append([row + 1, column + 2])
    except:
        pass
    try:
        temp = gameboard[row - 1][column + 2]
        if (parameter1.isupper() is gameboard[row-1][column+2].isupper()) and gameboard[row - 1][column + 2] != '  ':
            pass
        else:
            tempPossibleMoves.append([row - 1, column + 2])
    except:
        pass
    try:
        temp = gameboard[row - 2][column + 1]
        if (parameter1.isupper() is gameboard[row-2][column+1].isupper()) and gameboard[row - 2][column + 1] != '  ':
            pass
        else:
            tempPossibleMoves.append([row -2, column +1])
    except:
        pass
    try:
        temp = gameboard[row - 2][column - 1]
        if (parameter1.isupper() is gameboard[row-2][column-1].isupper()) and gameboard[row - 2][column - 1] != '  ':
            pass
        else:
            tempPossibleMoves.append([row - 2, column - 1])
    except:
        pass
    try:
        temp = gameboard[row - 1][column - 2]
        if (parameter1.isupper() is gameboard[row-1][column-2].isupper()) and gameboard[row - 1][column - 2] != '  ':
            pass
        else:
            tempPossibleMoves.append([row - 1, column - 2])
    except:
        pass
    try:
        temp = gameboard[row+1][column-1]
        if gameboard[row+1][column-1] == '  ':
            tempPossibleMoves.append([row+1, column-1])
    except:
        pass
    try:
        temp = gameboard[row-1][column-1]
        if gameboard[row-1][column-1] == '  ':
            tempPossibleMoves.append([row-1, column-1])
    except:
        pass
    try:
        temp = gameboard[row+1][column+1]
        if gameboard[row+1][column+1] == '  ':
            tempPossibleMoves.append([row+1, column+1])
    except:
        pass
    try:
        temp = gameboard[row+1][column-1]
        if gameboard[row+1][column-1] == '  ':
            tempPossibleMoves.append([row+1, column-1])
    except:
        pass
    # With temp variable I filtered all negative values.
    temp = [i for i in tempPossibleMoves if i[0] >= 0 and i[1] >= 0]
    possibleMoves = ["".join([index_to_letter[i[1]], str(i[0] + 1)]) for i in temp]
    possibleMoves.sort()
    return possibleMoves
"""------------------------------------------------------------------------------------------
A function that returns possible values for both white and black rooks for a given position.
"""
def rookPossibles(parameter1, positions, gameboard):
    column, row = list(positions[parameter1].strip().lower())
    row = int(row) - 1
    column = letter_to_index[column]
    tempPossibleMoves = []
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row+count][column]
            if (parameter1.isupper() is gameboard[row + count][column].isupper()) and gameboard[row + count][column] != '  ':
                break
            elif gameboard[row + count][column] == '  ':
                tempPossibleMoves.append([row+count, column])
            elif (parameter1.isupper() is not gameboard[row + count][column].isupper()) and gameboard[row + count][column] != '  ':
                tempPossibleMoves.append([row + count, column])
                break
    except:
        pass
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row-count][column]
            if (parameter1.isupper() is gameboard[row - count][column].isupper()) and gameboard[row - count][column] != '  ':
                break
            elif gameboard[row - count][column] == '  ':
                tempPossibleMoves.append([row - count, column])
            elif (parameter1.isupper() is not gameboard[row - count][column].isupper()) and gameboard[row - count][column] != '  ':
                tempPossibleMoves.append([row - count, column])
                break
    except:
        pass
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row][column + count]
            if (parameter1.isupper() is gameboard[row][column + count].isupper()) and gameboard[row][column + count] != '  ':
                break
            elif gameboard[row][column + count] == '  ':
                tempPossibleMoves.append([row, column + count])
            elif (parameter1.isupper() is not gameboard[row][column + count].isupper()) and gameboard[row][column + count] != '  ':
                tempPossibleMoves.append([row, column + count])
                break
    except:
        pass
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row][column - count]
            if (parameter1.isupper() is gameboard[row][column - count].isupper()) and gameboard[row][column - count] != '  ':
                break
            elif gameboard[row][column - count] == '  ':
                tempPossibleMoves.append([row, column - count])
            elif (parameter1.isupper() is not gameboard[row][column - count].isupper()) and gameboard[row][column - count] != '  ':
                tempPossibleMoves.append([row, column - count])
                break
    except:
        pass
    # With temp variable I filtered all negative values.
    temp = [i for i in tempPossibleMoves if i[0] >= 0 and i[1] >= 0]
    possibleMoves = ["".join([index_to_letter[i[1]], str(i[0] + 1)]) for i in temp]
    possibleMoves.sort()
    return possibleMoves
"""------------------------------------------------------------------------------------------
A function that returns possible values for both white and black bishops for a given position.
"""
def bishopPossibles(parameter1, positions, gameboard):
    column, row = list(positions[parameter1].strip().lower())
    row = int(row) - 1
    column = letter_to_index[column]
    tempPossibleMoves = []
    if 'b' in parameter1:
        try:
            count = 0
            while True:
                count += 1
                temp = gameboard[row + count][column + count]
                if (parameter1.isupper() is gameboard[row + count][column + count].isupper()) and gameboard[row + count][column + count] != '  ':
                    break
                elif gameboard[row + count][column + count] == '  ':
                    tempPossibleMoves.append([row + count, column + count])
                elif (parameter1.isupper() is not gameboard[row + count][column + count].isupper()) and gameboard[row + count][column + count] != '  ':
                    tempPossibleMoves.append([row + count, column + count])
                    break
        except:
            pass
        try:
            count = 0
            while True:
                count += 1
                temp = gameboard[row + count][column - count]
                if (parameter1.isupper() is gameboard[row + count][column - count].isupper()) and gameboard[row + count][column - count] != '  ':
                    break
                elif gameboard[row + count][column - count] == '  ':
                    tempPossibleMoves.append([row + count, column - count])
                elif (parameter1.isupper() is not gameboard[row + count][column - count].isupper()) and gameboard[row + count][column - count] != '  ':
                    tempPossibleMoves.append([row + count, column - count])
                    break
        except:
            pass
    elif 'B' in parameter1:
        try:
            count = 0
            while True:
                count += 1
                temp = gameboard[row - count][column + count]
                if (parameter1.isupper() is gameboard[row - count][column + count].isupper()) and gameboard[row - count][column + count] != '  ':
                    break
                elif gameboard[row - count][column + count] == '  ':
                    tempPossibleMoves.append([row - count, column + count])
                elif (parameter1.isupper() is not gameboard[row - count][column + count].isupper()) and gameboard[row - count][column + count] != '  ':
                    tempPossibleMoves.append([row - count, column + count])
                    break
        except:
            pass
        try:
            count = 0
            while True:
                count += 1
                temp = gameboard[row - count][column - count]
                if (parameter1.isupper() is gameboard[row - count][column - count].isupper()) and gameboard[row - count][column - count] != '  ':
                    break
                elif gameboard[row - count][column - count] == '  ':
                    tempPossibleMoves.append([row - count, column - count])
                elif (parameter1.isupper() is not gameboard[row - count][column - count].isupper()) and gameboard[row - count][column - count] != '  ':
                    tempPossibleMoves.append([row - count, column - count])
                    break
        except:
            pass
    # With temp variable I filtered all negative values.
    temp = [i for i in tempPossibleMoves if i[0] >= 0 and i[1] >= 0]
    possibleMoves = ["".join([index_to_letter[i[1]], str(i[0] + 1)]) for i in temp]
    possibleMoves.sort()
    return possibleMoves
"""------------------------------------------------------------------------------------------
A function that returns possible values for both white and black queens for a given position.
"""
def queenPossibles(parameter1, positions, gameboard):
    column, row = list(positions[parameter1].strip().lower())
    row = int(row) - 1
    column = letter_to_index[column]
    tempPossibleMoves = []
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row + count][column + count]
            if (parameter1.isupper() is gameboard[row + count][column + count].isupper()) and \
                    gameboard[row + count][column + count] != '  ':
                break
            elif gameboard[row + count][column + count] == '  ':
                tempPossibleMoves.append([row + count, column + count])
            elif (parameter1.isupper() is not gameboard[row + count][column + count].isupper()) and \
                    gameboard[row + count][column + count] != '  ':
                tempPossibleMoves.append([row + count, column + count])
                break
    except:
        pass
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row + count][column - count]
            if (parameter1.isupper() is gameboard[row + count][column - count].isupper()) and \
                    gameboard[row + count][column - count] != '  ':
                break
            elif gameboard[row + count][column - count] == '  ':
                tempPossibleMoves.append([row + count, column - count])
            elif (parameter1.isupper() is not gameboard[row + count][column - count].isupper()) and \
                    gameboard[row + count][column - count] != '  ':
                tempPossibleMoves.append([row + count, column - count])
                break
    except:
        pass
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row - count][column + count]
            if (parameter1.isupper() is gameboard[row - count][column + count].isupper()) and \
                    gameboard[row - count][column + count] != '  ':
                break
            elif gameboard[row - count][column + count] == '  ':
                tempPossibleMoves.append([row - count, column + count])
            elif (parameter1.isupper() is not gameboard[row - count][column + count].isupper()) and \
                    gameboard[row - count][column + count] != '  ':
                tempPossibleMoves.append([row - count, column + count])
                break
    except:
        pass
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row - count][column - count]
            if (parameter1.isupper() is gameboard[row - count][column - count].isupper()) and \
                    gameboard[row - count][column - count] != '  ':
                break
            elif gameboard[row - count][column - count] == '  ':
                tempPossibleMoves.append([row - count, column - count])
            elif (parameter1.isupper() is not gameboard[row - count][column - count].isupper()) and \
                    gameboard[row - count][column - count] != '  ':
                tempPossibleMoves.append([row - count, column - count])
                break
    except:
        pass
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row+count][column]
            if (parameter1.isupper() is gameboard[row + count][column].isupper()) and gameboard[row + count][column] != '  ':
                break
            elif gameboard[row + count][column] == '  ':
                tempPossibleMoves.append([row+count, column])
            elif (parameter1.isupper() is not gameboard[row + count][column].isupper()) and gameboard[row + count][column] != '  ':
                tempPossibleMoves.append([row + count, column])
                break
    except:
        pass
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row-count][column]
            if (parameter1.isupper() is gameboard[row - count][column].isupper()) and gameboard[row - count][column] != '  ':
                break
            elif gameboard[row - count][column] == '  ':
                tempPossibleMoves.append([row - count, column])
            elif (parameter1.isupper() is not gameboard[row - count][column].isupper()) and gameboard[row - count][column] != '  ':
                tempPossibleMoves.append([row - count, column])
                break
    except:
        pass
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row][column + count]
            if (parameter1.isupper() is gameboard[row][column + count].isupper()) and gameboard[row][column + count] != '  ':
                break
            elif gameboard[row][column + count] == '  ':
                tempPossibleMoves.append([row, column + count])
            elif (parameter1.isupper() is not gameboard[row][column + count].isupper()) and gameboard[row][column + count] != '  ':
                tempPossibleMoves.append([row, column + count])
                break
    except:
        pass
    try:
        count = 0
        while True:
            count += 1
            temp = gameboard[row][column - count]
            if (parameter1.isupper() is gameboard[row][column - count].isupper()) and gameboard[row][column - count] != '  ':
                break
            elif gameboard[row][column - count] == '  ':
                tempPossibleMoves.append([row, column - count])
            elif (parameter1.isupper() is not gameboard[row][column - count].isupper()) and gameboard[row][column - count] != '  ':
                tempPossibleMoves.append([row, column - count])
                break
    except:
        pass
    # With temp variable I filtered all negative values.
    temp = [i for i in tempPossibleMoves if i[0] >= 0 and i[1] >= 0]
    possibleMoves = ["".join([index_to_letter[i[1]], str(i[0] + 1)]) for i in temp]
    possibleMoves.sort()
    return possibleMoves
"""------------------------------------------------------------------------------------------
A function that returns possible values for both white and black kings for a given position.
"""
def kingPossibles(parameter1, positions, gameboard):
    column, row = list(positions[parameter1].strip().lower())
    row = int(row) - 1
    column = letter_to_index[column]
    tempPossibleMoves = []
    try:
        temp = gameboard[row + 1][column]
        if (parameter1.isupper() is gameboard[row + 1][column].isupper()) and gameboard[row + 1][column] != '  ':
            pass
        else:
            tempPossibleMoves.append([row + 1, column])
    except:
        pass
    try:
        temp = gameboard[row - 1]
        if (parameter1.isupper()) is (gameboard[row - 1][column].isupper()) and gameboard[row - 1][column] != '  ':
            pass
        else:
            tempPossibleMoves.append([row - 1, column])
    except:
        pass
    try:
        temp = gameboard[row + 1][column + 1]
        if (parameter1.isupper() is gameboard[row + 1][column + 1].isupper()) and gameboard[row + 1][column + 1] != '  ':
            pass
        elif gameboard[row + 1][column + 1] == '  ':
            tempPossibleMoves.append([row + 1, column + 1])
        elif (parameter1.isupper() is not gameboard[row + 1][column + 1].isupper()) and gameboard[row + 1][column + 1] != '  ':
            tempPossibleMoves.append([row + 1, column + 1])
    except:
        pass
    try:
        temp = gameboard[row + 1][column - 1]
        if (parameter1.isupper() is gameboard[row + 1][column - 1].isupper()) and gameboard[row + 1][column - 1] != '  ':
            pass
        elif gameboard[row + 1][column - 1] == '  ':
            tempPossibleMoves.append([row + 1, column - 1])
        elif (parameter1.isupper() is not gameboard[row + 1][column - 1].isupper()) and gameboard[row + 1][column - 1] != '  ':
            tempPossibleMoves.append([row + 1, column - 1])
    except:
        pass
    try:
        temp = gameboard[row - 1][column - 1]
        if (parameter1.isupper() is gameboard[row - 1][column - 1].isupper()) and gameboard[row - 1][column - 1] != '  ':
            pass
        elif gameboard[row - 1][column - 1] == '  ':
            tempPossibleMoves.append([row - 1, column - 1])
        elif (parameter1.isupper() is not gameboard[row - 1][column - 1].isupper()) and gameboard[row - 1][column - 1] != '  ':
            tempPossibleMoves.append([row - 1, column - 1])
    except:
        pass
    try:
        temp = gameboard[row - 1][column + 1]
        if (parameter1.isupper() is gameboard[row - 1][column + 1].isupper()) and gameboard[row - 1][column + 1] != '  ':
            pass
        elif gameboard[row - 1][column + 1] == '  ':
            tempPossibleMoves.append([row - 1, column + 1])
        elif (parameter1.isupper() is not gameboard[row - 1][column + 1].isupper()) and gameboard[row - 1][column + 1] != '  ':
            tempPossibleMoves.append([row - 1, column + 1])
    except:
        pass
    try:
        temp = gameboard[row][column + 1]
        if (parameter1.isupper() is gameboard[row][column + 1].isupper()) and gameboard[row][column + 1] != '  ':
            pass
        elif gameboard[row][column + 1] == '  ':
            tempPossibleMoves.append([row, column + 1])
        elif (parameter1.isupper() is not gameboard[row][column + 1].isupper()) and gameboard[row][column + 1] != '  ':
            tempPossibleMoves.append([row, column + 1])
    except:
        pass
    try:
        temp = gameboard[row][column - 1]
        if (parameter1.isupper() is gameboard[row][column - 1].isupper()) and gameboard[row][column - 1] != '  ':
            pass
        elif gameboard[row][column - 1] == '  ':
            tempPossibleMoves.append([row, column - 1])
        elif (parameter1.isupper() is not gameboard[row][column - 1].isupper()) and gameboard[row][column - 1] != '  ':
            tempPossibleMoves.append([row, column - 1])
    except:
        pass
    # With temp variable I filtered all negative values.
    temp = [i for i in tempPossibleMoves if i[0] >= 0 and i[1] >= 0]
    possibleMoves = ["".join([index_to_letter[i[1]], str(i[0] + 1)]) for i in temp]
    possibleMoves.sort()
    return possibleMoves
"""------------------------------------------------------------------------------------------
Showmoves function takes 3 parameters and transfer these parameters to specific functions to
be calculated and then takes a list as return value and returns this exact same value.
"""
def showmoves(parameter1, positions, gameboard):
    if 'p' in parameter1.casefold():
        return pawnPossibles(parameter1, positions, gameboard)
    elif 'n' in parameter1.casefold():
        return knightPossibles(parameter1, positions, gameboard)
    elif 'r' in parameter1.casefold():
        return rookPossibles(parameter1, positions, gameboard)
    elif 'b' in parameter1.casefold():
        return bishopPossibles(parameter1, positions, gameboard)
    elif 'q' in parameter1.casefold():
        return queenPossibles(parameter1, positions, gameboard)
    elif 'k' in parameter1.casefold():
        return kingPossibles(parameter1, positions, gameboard)
"""------------------------------------------------------------------------------------------
Current function prints the current situation of the gameboard according to the chess board rules.
"""
def current(gameboard):
    print('-----------------------')
    for x in gameboard[::-1]:
        for y in x:
            print('{0} '.format(y), end = '')
        print()
    print('-----------------------')
"""------------------------------------------------------------------------------------------
Move function takes 4 parameters, compare them and calculates the possibles list and returns a list.
"""
def move(parameter1, parameter2, positions, gameboard):
    column, row = list(positions[parameter1].strip().lower())
    row = int(row) - 1
    column = letter_to_index[column]
    invpositions = {v: k for k, v in positions.items()}
    if parameter2 in showmoves(parameter1, positions, gameboard):
        try:
                if (parameter1.isupper() is invpositions[parameter2]) and gameboard[row][column] != '  ':
                    print('FAILED')
                else:
                    if invpositions[parameter2].casefold() != 'ki':
                        print('OK')
                        gameboard[row][column] = '  '
                        positions[parameter1] = parameter2
                        column, row = list(positions[parameter1].strip().lower())
                        row = int(row) - 1
                        column = letter_to_index[column]
                        gameboard[row][column] = parameter1
                    else:
                        print('FAILED')
        except:
                print('OK')
                gameboard[row][column] = '  '
                positions[parameter1] = parameter2
                column, row = list(positions[parameter1].strip().lower())
                row = int(row) - 1
                column = letter_to_index[column]
                gameboard[row][column] = parameter1
    else:
        print('FAILED')
"""------------------------------------------------------------------------------------------
I created a loop that iterates on commands list. Through this list it executes all commands until the 'exit'
command. This loop looks up the first element of the every single command and transfer the parameters to
these specific functions.
"""
for i in commands:
    if i[0] == 'showmoves':
        parameter1 = i[1]
        print('> showmoves {0}'.format(parameter1))
        if not showmoves(parameter1, positions, gameboard):
            print('FAILED')
        else:
            for i in showmoves(parameter1, positions, gameboard):
                print(i + ' ', end='')
            print()
    elif i[0] == 'print':
        print('> print')
        current(gameboard)
    elif i[0] == 'exit':
        print('> exit')
        exit()
    elif i[0] == 'initialize':
        print('> initialize\nOK')
        positions = {'r1': 'a1', 'n1': 'b1', 'b1': 'c1', 'qu': 'd1', 'ki': 'e1', 'b2': 'f1', 'n2': 'g1', 'r2': 'h1',
                     'p1': 'a2', 'p2': 'b2', 'p3': 'c2', 'p4': 'd2', 'p5': 'e2', 'p6': 'f2', 'p7': 'g2', 'p8': 'h2',
                     'R1': 'a8', 'N1': 'b8', 'B1': 'c8', 'QU': 'd8', 'KI': 'e8', 'B2': 'f8', 'N2': 'g8', 'R2': 'h8',
                     'P1': 'a7', 'P2': 'b7', 'P3': 'c7', 'P4': 'd7', 'P5': 'e7', 'P6': 'f7', 'P7': 'g7', 'P8': 'h7'}
        gameboard = [['R1', 'N1', 'B1', 'QU', 'KI', 'B2', 'N2', 'R2'],
                     ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],
                     ['r1', 'n1', 'b1', 'qu', 'ki', 'b2', 'n2', 'r2']]
        gameboard.reverse()
        current(gameboard)
    elif i[0] == 'move':
        print('> move {0} {1}'.format(i[1], i[2]))
        parameter1 = i[1]
        parameter2 = i[2]
        move(parameter1, parameter2, positions, gameboard)
