# Abdullah Mert Dinçer
# b2200356016
# 8-October-2020
import sys

S = (sys.argv[1])                                             # Gets the first argument
split_S = str.split(S, ',')                                   # Removes the commas in string
int_split_S = []
evens_S = []
positive_S = []
sum_of_evens = 0
sum_positives = 0

for i in range (0, len(split_S)):                             # This function takes the values from split string list and...
    int_split_S.append(int(split_S[i]))                       # ... add them to int_split_list which is list for integers split from the string.

for i in range (0, len(int_split_S)):                         # This function starts from the firs element of the list and continues up to last element.
    if int_split_S[i] > 0:                                    # Determines whether the integers in the list are positive or not.
        positive_S.append(int_split_S[i])                     # If there are positives they are appended to positive_S list.
        if int_split_S[i] % 2 == 0:                           # This if condition takes the even ones add them to list called evens_S.
            evens_S.append(int_split_S[i])

for i in range (0, len(evens_S)):                             # This 2 lines of codes sums all even numbers.
    sum_of_evens += evens_S[i]

for i in range (0, len(evens_S)):                             # This part here prints all the even numbers to the screen.
    if i == 0:
        print('Even Numbers: ' + '"' + str(evens_S[i]), end="")
    elif i in range (1, len(evens_S) - 1):
        print("," + str(evens_S[i]), end="")
    else:
        print("," + str(evens_S[i]) + '"')

for i in range (0, len(positive_S)):                          # This part sums all the positive numbers.
    sum_positives += positive_S[i]

print("Sum of Even Numbers:", str(sum_of_evens))
print("Even Number Rate:", str(sum_of_evens / sum_positives)) # Prints the even number rate.
