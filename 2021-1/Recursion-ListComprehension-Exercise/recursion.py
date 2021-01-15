import sys

n = int(sys.argv[1])
strlst1 = ['*' * i for i in range(1, n+1)]
strlst2 = ['*' * i for i in range(n-1, 0, -1)]
finalList = strlst1 + strlst2

for i in range(1, 2*n):
    if i <= n:
        print((n-i) * ' ' + (2*i - 1) * '*')
    else:
        print((i-n) * ' ' + (2 * (n - (i%n)) - 1) * '*')