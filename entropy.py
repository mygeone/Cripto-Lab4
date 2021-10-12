import re, math

def checkNumbers(string):
    return 10 if re.search('[0-9]',string) else 0

def checkCaseInsensitive(string):
    return 26 if(re.search('[a-z]',string)) else 0

def checkCaseInsensitive2(string):
    return 26 if(re.search('[A-Z]',string)) else 0

def checkSymbols(string):
    return 32 if(re.search('[\W]',string)) else 0

def entropy(password, verbose):
    base = checkNumbers(password) + checkCaseInsensitive(password) + checkCaseInsensitive2(password) + checkSymbols(password)
    entr = math.log2(pow(base,len(password)))
    if(verbose):
        print("La base calculada para la password es: ",base)
        print("El largo de la password es: ",len(password))
        print("La formula utilizada es: H = log2(N^L)")
        print("La entropia calculada es: ",entr)
    else:
        print(password+" | "+str(entr))