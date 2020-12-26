# Abdullah Mert Dinçer
# 8-October-2020

import sys
import math

coefficient_x2 = float(sys.argv[1])                   # Takes input as argv
coefficient_x = float(sys.argv[2])
constant = float(sys.argv[3])

discriminant = (coefficient_x ** 2) - (4 * coefficient_x2 * constant)

solution_1 = ((-1 * coefficient_x) + (math.sqrt(discriminant))) / (2 * coefficient_x2)
solution_2 = ((-1 * coefficient_x) - (math.sqrt(discriminant))) / (2 * coefficient_x2)

if discriminant > 0:
    print("There are two solutions\n" + "Solution(s): " + "{0} {1}".format(solution_1, solution_2))        # Prints if there are two real solutions.
elif discriminant == 0:
    print("Quadratic has a repeated real number solution\n" + "Solution: " + "{0}".format(solution_1))     # Prints if there is one repeated solution.
else:
    print("Quadratic has no real solutions. Neither of the roots are real.")                               # Prints if there is no real roots.
