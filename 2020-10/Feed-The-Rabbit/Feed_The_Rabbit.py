# Abdullah Mert Dinçer
# b2200356016
# 14-October-2020
# Feed The Rabbit

row_counter = -1                                                            # I initialized row_counter with a value of -1 because program counts...
str_gameBoard = input('Please enter feeding map as a list:\n')              # ...open square brackets and input will include 1 extra of them.
str_directions = input('Please enter direction of movements as a list:\n')
list_gameBoard = []
list_directions = []
direction_counter = 1                                                             # I initialized direction_counter as 1 because program counts the commas...
total_positions = initial_position = score = move_counter = first_position = 0    # ...in the input and input lacks one.
is_poison = False                                        # If rabbit eats the poison it will be dead so in the first i initialized poison status as False.

for c in str_gameBoard:                                  # This loop splits the input and add necessary values to list.
    if c == '[':                                         # It also counts the '[' to find how many rows are there.
        row_counter += 1
    if c == 'W' or c == 'X' or c == 'C' or c == 'A' or c == 'P' or c == 'M' or c == '*':
        list_gameBoard.append(c)
        total_positions += 1
        if c == '*':                                     # This condition here will be processed if c is '*' and to know first position...
            initial_position = total_positions           # ...the calculated initial position will be copied to first position...
            first_position = initial_position            # ...In the next steps initial_position will be changed with respect to directions...
                                                         # ...but first_position will be constant.
column_counter = total_positions // row_counter          # This command here finds the column number by dividing total position by row number.


def draw_gameBoard():                                    # This function creates the game board according to datas which were collected in the previous steps.
    coefficient = 1                                      # Coefficient is used for creating the next rows of game board.
    for i in range(total_positions):
        if (i+1) == coefficient * column_counter:
            coefficient += 1
            print(list_gameBoard[i])
        else:
            print(list_gameBoard[i] + ' ', end='')


for c in str_directions:                                # This loop finds how many directions are there in given input...
    if c == ',':                                        # ...by counting the number of commas...
        direction_counter += 1                          # ...However, input will have one missing comma that's why I initialized...
    if c == 'U' or c == 'D' or c == 'R' or c == 'L':    # direction_counter variable as 1.
        list_directions.append(c)


def which_direction(parameter):                         # This function here is vital. It is the one who moves the rabbit and calculates the score.
    global is_poison, first_position, move_counter, score, initial_position, list_gameBoard, column_counter
    if list_gameBoard[initial_position - 1 + parameter] == 'A':                         # initial_position means current position. It is not first position.
        score += 5                                                                      # This function takes the current position's index number and...
    elif list_gameBoard[initial_position - 1 + parameter] == 'C':                       # ...takes a parameter to perform which operation. (L, R, U, D)...
        score += 10
    elif list_gameBoard[initial_position - 1 + parameter] == 'M':
        score -= 5
    elif list_gameBoard[initial_position - 1 + parameter] == 'P':                       # If poison is eaten, is_poison will be changed to True and program...
        list_gameBoard[initial_position - 1 + parameter] = '*'                          # will no longer run. It will output final position and score.
        list_gameBoard[initial_position - 1] = 'X'
        list_gameBoard[first_position - 1] = 'X'
        is_poison = True
        return score
    list_gameBoard[initial_position - 1 + parameter] = 'X'                             # Program will think that move as not last move but a continous one.
    initial_position = initial_position + parameter                                    # So it will change the value of current position's index as 'X'.


# This function evaluates every possible movement choice in each block. And then it determines which parameter will be used to call the direction function.
def update_gameBoard():
    global is_poison, first_position, move_counter, score, initial_position, list_gameBoard, column_counter, row_counter
    if not is_poison:
        for i in range(direction_counter):
            if not is_poison:
                move_counter += 1
                # This if condition will be executed for blocks that do not touch the borders. (i.e. inner blocks)
                if initial_position % column_counter != 1 and initial_position % column_counter != 0 and initial_position > column_counter and initial_position <= total_positions - column_counter:
                    if list_directions[i] == 'U' and list_gameBoard[initial_position-1-column_counter] != 'W':
                        which_direction(-column_counter)
                    elif list_directions[i] == 'D' and list_gameBoard[initial_position-1+column_counter] != 'W':
                        which_direction(column_counter)
                    elif list_directions[i] == 'L' and list_gameBoard[initial_position-1-1] != 'W':
                        which_direction(-1)
                    elif list_directions[i] == 'R' and list_gameBoard[initial_position-1+1] != 'W':
                        which_direction(1)
                # This condition will be executed for block that touches very left border.
                elif initial_position % column_counter == 1:
                    if initial_position == 1 or initial_position == (row_counter - 1) * column_counter + 1:
                        if initial_position == 1:
                            if list_directions[i] == 'D' and list_gameBoard[initial_position-1+column_counter] != 'W':
                                which_direction(column_counter)
                            elif list_directions[i] == 'R' and list_gameBoard[initial_position-1+1] != 'W':
                                which_direction(1)
                        elif initial_position == (row_counter - 1) * column_counter + 1:
                            if list_directions[i] == 'U' and list_gameBoard[initial_position - 1 - column_counter] != 'W':
                                which_direction(-column_counter)
                            elif list_directions[i] == 'R' and list_gameBoard[initial_position - 1 + 1] != 'W':
                                which_direction(1)
                    else:
                        if list_directions[i] == 'D' and list_gameBoard[initial_position - 1 + column_counter] != 'W':
                            which_direction(column_counter)
                        elif list_directions[i] == 'U' and list_gameBoard[initial_position - 1 - column_counter] != 'W':
                            which_direction(-column_counter)
                        elif list_directions[i] == 'R' and list_gameBoard[initial_position - 1 + 1] != 'W':
                            which_direction(1)
                # It will be executed for block that touches very right border.
                elif initial_position % column_counter == 0:
                    if initial_position == column_counter or initial_position == total_positions:
                        if initial_position == column_counter:
                            if list_directions[i] == 'D' and list_gameBoard[initial_position-1+column_counter] != 'W':
                                which_direction(column_counter)
                            elif list_directions[i] == 'L' and list_gameBoard[initial_position-1-1] != 'W':
                                which_direction(-1)
                        elif initial_position == total_positions:
                            if list_directions[i] == 'U' and list_gameBoard[initial_position - 1 - column_counter] != 'W':
                                which_direction(-column_counter)
                            elif list_directions[i] == 'L' and list_gameBoard[initial_position - 1 - 1] != 'W':
                                which_direction(-1)
                    else:
                        if list_directions[i] == 'D' and list_gameBoard[initial_position - 1 + column_counter] != 'W':
                            which_direction(column_counter)
                        elif list_directions[i] == 'U' and list_gameBoard[initial_position - 1 - column_counter] != 'W':
                            which_direction(-column_counter)
                        elif list_directions[i] == 'L' and list_gameBoard[initial_position - 1 - 1] != 'W':
                            which_direction(-1)
                # This condition will be executed for upper and lower block that touches the border.
                else:
                    if initial_position < column_counter:
                        if list_directions[i] == 'D' and list_gameBoard[initial_position - 1 + column_counter] != 'W':
                            which_direction(column_counter)
                        elif list_directions[i] == 'L' and list_gameBoard[initial_position - 1 - 1] != 'W':
                            which_direction(-1)
                        elif list_directions[i] == 'R' and list_gameBoard[initial_position - 1 + 1] != 'W':
                            which_direction(1)
                    elif initial_position > column_counter * (row_counter - 1) + 1:
                        if list_directions[i] == 'U' and list_gameBoard[initial_position - 1 - column_counter] != 'W':
                            which_direction(-column_counter)
                        elif list_directions[i] == 'L' and list_gameBoard[initial_position - 1 - 1] != 'W':
                            which_direction(-1)
                        elif list_directions[i] == 'R' and list_gameBoard[initial_position - 1 + 1] != 'W':
                            which_direction(1)
        if (move_counter == direction_counter) and (not is_poison):
            list_gameBoard[first_position - 1] = 'X'
            list_gameBoard[initial_position - 1] = '*'
    return score


print('Your board is:')
draw_gameBoard()
update_gameBoard()
print('Your output should be like this:')
draw_gameBoard()
print('Your score is: {}'.format(score))
