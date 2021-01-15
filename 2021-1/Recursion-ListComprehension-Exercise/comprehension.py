import sys

n = int(sys.argv[1])
count = (2 * n) - 1
finalList = []
def recurDiamond(count, n, lst):
    if count == 1:
        str1 = (n-1) * ' ' + '*'
        finalList.append(str1)
        return finalList
    else:
        if count >= n:
            str1 = (count % n) * ' ' + (2*(((2*n)) - count)-1) * '*'
            lst.append(str1)
        else:
            str1 = (n-(count % n)) * ' ' + (2*count - 1) * '*'
            lst.append(str1)
        recurDiamond(count - 1, n, lst)
recurDiamond(count, n, finalList)
for i in finalList:
    print(i)