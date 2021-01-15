# Abdullah Mert Dinçer
# b2200356016
# 22-December-2020
# Encrypt/Decrypt
#------------------------------------------------------------------------------------------
import sys
import os

class ParameterNumberError(Exception):
    pass
class UndefinedParameterError(Exception):
    pass
class NotReadableError(Exception):
    pass
class FileIsEmptyError(Exception):
    pass
try:
    if len(sys.argv) != 5:
        raise ParameterNumberError
    errorfile = 'Key file'
    f = open(sys.argv[2], 'r')
    keyMatrix = [line.strip('\n').split(',') for line in f if line != '\n']
    f.close()
    notreadablefile = 'Key File'
    if sys.argv[2][-4:] != '.txt':
        raise NotReadableError
    emptyfile = 'Key File'
    if os.stat(sys.argv[2]).st_size == 0:
        raise FileIsEmptyError
    erroryfile = 'key file'
    # Here I initialized keyMatrix with the given values in key.txt file.
    for submatrix in keyMatrix:
        for j in range(len(submatrix)):
            submatrix[j] = int(submatrix[j])
    alpha_to_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
                    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27}

    num_to_alpha = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
                    15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z', 27: ' '}
    #------------------------------------------------------------------------------------------
    def divideString(string, n):
        """This function takes string input and divides it to n pieces
        with respect to keyMatrix size.txt

        Args:
            string (str): string that will be divided
            n (int): size of matrix for instance in a 3x3 matrix n = 3

        Returns:
            list: list that consists of n sized divided string pieces
        """
        str_size = len(string)
        if str_size % n != 0:
            x = str_size % n
            string += (' ' * (n-x))
        part_size = n
        j = 1
        str1 = ''
        plaintextlist = []
        for i in string:
            if j % part_size == 0:
                str1 += i
                plaintextlist.append(str1)
                str1 = ''
            else:
                str1 += i
            j += 1
        return plaintextlist
    #------------------------------------------------------------------------------------------
    def AlphaToNumConverter(list, dict):
        """This function converts the letters to corresponding numbers.

        Args:
            list (list): list that will be converted
            dict (dictionary): dictionary that will be used while converting

        Returns:
            list: convertedMatrix nx1 size
        """
        convertedMatrix = []
        for i in list:
            lst = []
            for j in i:
                number = dict[j.upper()]
                lst.append([number])
            convertedMatrix.append(lst)
        return convertedMatrix
    #------------------------------------------------------------------------------------------
    def matrixMultiplier(CMatrix, KMatrix):
        """This function multiplies two matrices

        Args:
            CMatrix (list): matrix that is converted from n sized string pieces.
            KMatrix (list): keyMatrix

        Returns:
            list: a list that is encoded
        """
        result = [[0] for i in range(len(CMatrix))]
        for i in range(len(KMatrix)):
            for j in range(len(CMatrix[0])):
                for k in range(len(CMatrix)):
                    result[i][j] += KMatrix[i][k] * CMatrix[k][j]
        return result
    #------------------------------------------------------------------------------------------
    def matrixInverseCalculator(KMatrix):
        """A function that calculates the inverse of a matrix by using Gauss-Jordan Method

        Args:
            KMatrix (list): Key Matrix that will be inverted

        Returns:
            list: Inverted Matrix
        """
        length = len(KMatrix)
        inverseMatrix = []
        for i in range(length):
            templist = []
            for j in range(length):
                templist.append(0)
            inverseMatrix.append(templist)
        for i in range(length):
            for j in range(length):
                if i == j:
                    inverseMatrix[i][j] = 1
                else:
                    pass
        for i in range(length):
            d = KMatrix[i][i]
            for j in range(length):
                KMatrix[i][j] = KMatrix[i][j]/d
                inverseMatrix[i][j] = inverseMatrix[i][j]/d
            for m in range(length):
                if m != i:
                    k = KMatrix[m][i]
                    for j in range(length):
                        KMatrix[m][j] = KMatrix[m][j] - (KMatrix[i][j] * k)
                        inverseMatrix[m][j] = inverseMatrix[m][j] - (inverseMatrix[i][j] * k)
        for i in range(length):
            for j in range(length):
                inverseMatrix[i][j] = round(inverseMatrix[i][j])
        return inverseMatrix
    #------------------------------------------------------------------------------------------
    if sys.argv[1].casefold() == 'enc':
        errorfile = 'Input file'
        f = open(sys.argv[3], 'r')
        notreadablefile = 'Input File'
        if sys.argv[3][-4:] != '.txt':
            raise NotReadableError
        emptyfile = 'Input File'
        if os.stat(sys.argv[3]).st_size == 0:
            raise FileIsEmptyError
        plaintext = f.readlines()
        f.close()
        plaintextList = divideString(plaintext[0], len(keyMatrix))
        invalidCfile = 'input file'
        convertedMatrix = AlphaToNumConverter(plaintextList, alpha_to_num)
        f = open(sys.argv[4], 'w')
        count = 1
        for x in range(len(convertedMatrix)):
            # This for loop here writes the coded message to file.
            for y in matrixMultiplier(convertedMatrix[x], keyMatrix):
                for z in y:
                    if count == len(convertedMatrix)*len(convertedMatrix[0]):
                        f.write(str(z))
                    else:
                        f.write(str(z))
                        f.write(',')
                    count += 1
        f.close()
    elif sys.argv[1].casefold() == 'dec':
        errorfile = 'Input file'
        f = open(sys.argv[3], 'r')
        notreadablefile = 'Input File'
        if sys.argv[3][-4:] != '.txt':
            raise NotReadableError
        emptyfile = 'Input File'
        if os.stat(sys.argv[3]).st_size == 0:
            raise FileIsEmptyError
        ciphertext = f.readlines()
        f.close()
        ciphertextList = ciphertext[0].split(',')
        templist = []
        count = 1
        cipherDividedList = []
        erroryfile = 'input file'
        for s in ciphertextList:
            # This for loop here creates a list that consists of encoded numbers.
            if count == len(keyMatrix):
                templist.append([int(s)])
                cipherDividedList.append(templist)
                count = 1
                templist = []
            else:
                templist.append([int(s)])
                count += 1
        inverseMatrix = matrixInverseCalculator(keyMatrix)
        count = 1
        f = open(sys.argv[4], 'w')
        invalidCfile = 'key file'
        for x in range(len(cipherDividedList)):
            for y in matrixMultiplier(cipherDividedList[x], inverseMatrix):
                for z in y:
                    a = num_to_alpha[z]
                    f.write(a)
        f.close()
    else:
        raise UndefinedParameterError

except ParameterNumberError:
    print('Parameter number error')
except UndefinedParameterError:
    print('Undefined parameter error')
except FileNotFoundError:
    print(errorfile, 'not found error')
except NotReadableError:
    if notreadablefile == 'Input File':
        print('The input file could not be read error')
    elif notreadablefile == 'Key File':
        print('Key file could not be read error')
except FileIsEmptyError:
    print(emptyfile, 'is empty error')
except KeyError:
    print('Invalid character in', invalidCfile, 'error')
except ValueError:
    print('Invalid character in', erroryfile, 'file error')
except ZeroDivisionError:
    print('Invalid character in key file error')
#------------------------------------------------------------------------------------------
