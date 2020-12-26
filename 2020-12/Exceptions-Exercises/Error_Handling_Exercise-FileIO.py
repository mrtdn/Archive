# Abdullah Mert Dinçer
# 20-December-2020

import sys
import math
oneortwo = 1
# If there's an error it will be thrown and will be caught by one of exceptions block.
try:
    file = open(sys.argv[1], 'r')
    nonemptylines = [line.strip('\n') for line in file if line != '\n']
    file.close()
    lst = []
    tempsolutionlst = []
    solutionlst = []
    oneortwo = 2
    file = open(sys.argv[2], 'r')
    comparisondata = [line.strip('\n') for line in file if line != '\n']
    file.close()
    comparisonlst = []
    count = -1
    count2 = -1
    for i in nonemptylines:
        lst.append([j for j in i.split()])
    for i in comparisondata:
        comparisonlst.append([j for j in i.split()])
    for i in lst:
        count2 += 1
        try:
            if len(i) >= 5:
                raise Exception
            for j in range(math.floor(float(i[2])), math.floor(float(i[3]))+1):
                if (j % math.floor(float((i[0]))) == 0) and (j % math.floor(float((i[1]))) != 0):
                    tempsolutionlst.append(j)
            solutionlst.append(tempsolutionlst)
            tempsolutionlst = []
            count += 1
            str1 = ' '.join(str(e) for e in solutionlst[count])
            comparisonstr1 = ' '.join(str(e) for e in comparisonlst[count2])
            try:
                assert str1 == comparisonstr1
                print('------------')
                print(f'My results:               {str1}')
                print(f'Results to compare:       {comparisonstr1}')
                print('Goool!!!')
            except AssertionError:
                print('------------')
                print(f'My results:               {str1}')
                print(f'Results to compare:       {comparisonstr1}')
                print('Assertion Error: results don’t match.')
        except ValueError:
            tmpstr = ' '.join(x for x in i)
            print('------------')
            print('ValueError: only numeric input is accepted.')
            print(f'Given input: {tmpstr}')
        except IndexError:
            tmpstr = ' '.join(x for x in i)
            print('------------')
            print('IndexError: number of operands less than expected.')
            print(f'Given input: {tmpstr}')
        except ZeroDivisionError:
            tmpstr = ' '.join(x for x in i)
            print('------------')
            print('ZeroDivisionError: You can’t divide by 0.')
            print(f'Given input: {tmpstr}')
        except:
            print('------------')
            print('kaBOOM: run for your life!')
        else:
            pass
except IndexError:
    print('IndexError: number of input files less than expected.')
except FileNotFoundError:
    print(f'IOError: cannot open {sys.argv[oneortwo]}')
except:
    print('------------')
    print('kaBOOM: run for yourlife!')
finally:
    print()
    print(' ̃ Game Over ̃')
