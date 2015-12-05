def StringToInt(stringNumber):
    retVal = '99'

    stringNumber = stringNumber.strip()

    if stringNumber == "zero":
        retVal = '0'
    elif stringNumber == "one":
        retVal = '1'
    elif stringNumber == "two":
        retVal = '2'
    elif stringNumber == "three":
        retVal = '3'
    elif stringNumber == "four":
        retVal = '4'
    elif stringNumber == "five":
        retVal = '5'
    elif stringNumber == "six":
        retVal = '6'
    elif stringNumber == "seven":
        retVal = '7'
    elif stringNumber == "eight":
        retVal = '8'
    elif stringNumber == "nine":
        retVal = '9'

    return retVal

def ParseInput(data):
    values = data.split(';')
    
    digit = ''

    for val in values:
        digit += StringToInt(val)
    
    print digit

def main():
    inputFile = open('input.txt','r')

    stringInput = inputFile.readlines()

    for line in stringInput:
        ParseInput(line)

    inputFile.close()

main()
