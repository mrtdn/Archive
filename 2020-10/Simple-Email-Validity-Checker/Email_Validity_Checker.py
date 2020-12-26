# Abdullah Mert Dinçer
# b2200356016
# 6-October-2020

def validityChecker(email):                                     # This function checks the if input has
    if "." in email and "@" in email:                           # "." and "@" characters in its
        print("Your email is valid.")                           # If it is false it prints out an error message
    else:
        print("Your email is not valid!")

email = input("Please enter your email: ")
validityChecker(email)                                         # Calling function




