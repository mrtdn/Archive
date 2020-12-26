nonprimes = [x for x in range(2, 50) for y in range(2, x) if (x % y) == 0]
nonprimes = list(set(nonprimes))
primes = [x for x in range(2, 50) if x not in nonprimes]
print(nonprimes)
print(primes)