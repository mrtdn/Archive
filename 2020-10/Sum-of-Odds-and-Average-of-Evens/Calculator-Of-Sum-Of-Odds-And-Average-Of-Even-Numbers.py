# Abdullah Mert Dinçer
# b2200356016
# 6-October-2020

try:
    # Variables initialized.
    number_of_evens = sum_of_odds = sum_of_evens = 0
    number = int(input("Please enter an upper limit higher than 1 for calculation (your number will be included): "))

    for i in range(1, number + 1):                                     # This function takes a value from user.
                                                                        # Assign this value as upper limit (included) for function.
        if (i % 2) == 1:                                                # Interval is {1, 2, ..., n}
            sum_of_odds += i                                            # If the numbers in interval are odd it calculates the sum of them(odd numbers).
        else:                                                           # If the numbers in interval are even it calculates the average value of them.
            sum_of_evens += i                                           # After calculation it prints "Sum of odds" and "Average of evens"
            number_of_evens += 1

    avg_of_evens = sum_of_evens // number_of_evens
    print("Sum of odds is: {}".format(sum_of_odds))
    print("Average of evens is: {}".format(avg_of_evens))

except:

    print("Error! Enter a valid number.")                              # If the number is not greater than 1 the program will print out an error message!