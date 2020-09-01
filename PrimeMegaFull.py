import math
primes = []

def getprimes(min, max):
    with open("C:\\Users\\deuce\\Desktop\\pythonProjects\\primelist.txt", 'r') as primefile:
        for line in primefile:
            if int(line) >= min:
                primes.append(int(line))
            elif int(line) > max:
                break
    return primes
    
def primeFactorize(x):
    y = 0
    xFactors = [1]
    getprimes(0, math.floor(x / 2))
    while math.prod(xFactors) < x:
        if (x / math.prod(xFactors)) % primes[y] == 0:
            xFactors.append(primes[y])
        else:
            y += 1
    del xFactors[0]
    return xFactors

def lcm(numbers):
    lcmFactorList = []
    lcmFactorList1D = []
    for f in numbers:
        lcmFactorList.append(primeFactorize(f))
    i = 0
    for g in lcmFactorList:
        for h in g:
            if lcmFactorList[i].count(h) > lcmFactorList1D.count(h):
                lcmFactorList1D.append(h)
        i += 1
    return math.prod(lcmFactorList1D)

def gcf(gcfNumbers):
    gcfFactorList = []
    gcfFactorList1D = []
    for l in gcfNumbers:
        gcfFactorList.append(primeFactorize(l))
    r = 0
    for p in gcfFactorList:
        for q in p:
            if q in gcfFactorList1D:
                if gcfFactorList[r].count(q) > gcfFactorList1D.count(q):
                    countDifference = gcfFactorList[r].count(
                        q) - gcfFactorList1D.count(q)
                    while countDifference > 0:
                        gcfFactorList1D.append(q)
                        countDifference -= 1
            else:
                countDifference = gcfFactorList[r].count(q)
                while countDifference > 0:
                    gcfFactorList1D.append(q)
                    countDifference -= 1
        r += 1
    s = 0
    for n in gcfFactorList:
        for o in n:
            m = 0
            while m < len(gcfNumbers):
                if o in gcfFactorList[m]:
                    if gcfFactorList[s].count(o) < gcfFactorList1D.count(o):
                        countDifference = gcfFactorList1D.count(
                            o) - gcfFactorList[s].count(o)
                        while countDifference > 0:
                            gcfFactorList1D.remove(o)
                            countDifference -= 1
                else:
                    countDifference = gcfFactorList1D.count(o)
                    while countDifference > 0:
                        gcfFactorList1D.remove(o)
                        countDifference -= 1
                m += 1
        s += 1
    return math.prod(gcfFactorList1D)

def simplifyRadical(index, radicand):
    floatcount = 0
    radicandOutside = []
    radicandInside = []
    while type(radicand) is float:
        if radicand % 1 == 0:
            radicand = int(radicand)
        else:
            radicand *= 10
            floatcount += 1
    for u in primeFactorize(radicand):
        radicandInside.append(u)
    for t in radicandInside:
        if radicandInside.count(t) >= index:
            radicandOutside.append(t)
            v = 0
            while v < index:
                radicandInside.remove(t)
                v += 1
    if (math.prod(radicandInside) / (10 ** floatcount)) % 1 == 0:
        CONVradicandInside = int(math.prod(radicandInside) / (10 ** floatcount))
    else:
        CONVradicandInside = math.prod(radicandInside) / (10 ** floatcount)
    return index, math.prod(radicandOutside), CONVradicandInside

def generateMorePrimes(limit):
    possprime = []
    with open("C:\\Users\\deuce\\Desktop\\pythonProjects\\primelist.txt", 'r') as primefile:
        for line in primefile:
            primes.append(int(line))
    x = primes[-1] + 2
    while x <= limit:
        b = 0
        while primes[b] <= math.sqrt(x):
            if not x % primes[b] == 0:
                if not x in possprime:
                    possprime.append(x)
                b += 1
            else:
                if x in possprime:
                    possprime.remove(x)
                break
        if x in possprime:
            primes.append(x)
            with open('C:\\Users\\deuce\\Desktop\\pythonProjects\\primelist.txt', 'a') as primefile:
                primefile.write('\n')
                primefile.write(str(x))
            print(x)
        x += 2

again = 'yes'
print('\nHello. Welcome to a small collection of slightly useful mathematical functions. Please only input integers.')
choice = False
while again == 'yes':
    while type(choice) is not int:
        try:
            choice = int(input("""\nThere are 4 functions. Input the number corresponding to the function you want to use. 
        \b\b\b\b\b\b\b\b\b\b- Get a list of primes within a chosen range. [1] 
        \b\b\b\b\b\b\b\b\b\b- Generate the prime factorization of a number. [2] 
        \b\b\b\b\b\b\b\b\b\b- Generate the least common multiple of a set of numbers. [3] 
        \b\b\b\b\b\b\b\b\b\b- Generate the greatest common factor of a set of numbers. [4]
        \b\b\b\b\b\b\b\b\b\b- Simplify a radical. [5]
        \b\b\b\b\b\b\b\b\b\b- Generate more primes and save to a .txt file. [6]

        \b\b\b\b\b\b\b\b\b\bChoose a function: """))
            if choice < 1 or choice > 6:
                print('\nPlease choose an integer 1-5.')
                choice = False
        except:
            print('\nPlease choose an integer 1-5.')
            choice = False
    if choice == 1:
        minimum = False
        maximum = False
        again = 0
        while type(minimum) is not int or type(maximum) is not int:
            try:
                minimum = int(
                    input('\nChoose a non-negative integer to be the minimum of the range: '))
                maximum = int(input('\nChoose an integer greater than the minumum and less than 100000 to be the maximum of the range: '))
                if maximum <= minimum:
                    print('\nPlease choose a maximum greater than the minimum.')
                    minimum = False
                    maximum = False
                elif minimum < 0:
                    print('\nPlease choose a non-negative integer.')
                    minimum = False
                    maximum = False
                elif maximum > 100000:
                    print('\nPlease choose a number less than 100000.')
                    minimum = False
                    maximum = False
            except:
                print('\nPlease choose valid integers.')
                minimum = False
                maximum = False
        print('\nPrimes: ', getprimes(minimum, maximum))
        choice = False
    elif choice == 2:
        factorend = False
        while type(factorend) is not int or factorend <= 0:
            try:
                factorend = int(input('\nInput a positive integer you want the prime factorization of: '))
                if factorend <= 0:
                    print('\nPlease choose a positive integer.')
                    factorend = False
            except:
                print('\nPlease choose a positive integer.')
                factorend = False
        print('\nPrime Factorization: ', primeFactorize(factorend))
        choice = False
    elif choice == 3:
        lcmUserInputList = []
        lcmUserInputInt = False
        while type(lcmUserInputInt) is not int or lcmUserInputInt <= 0 or lcmUserInputInt > 1000000000000:
            try:
                lcmUserInputInt = int(input('\nChoose a positive integer less than 1,000,000,000,000: '))
                lcmUserInputList.append(lcmUserInputInt)
            except:
                print('\nPlease choose a positive integer less than 1,000,000,000,000.')
                lcmUserInputInt = False
            lcmUserInputInt = input('\nWould you like to choose another number for the LCM? Type anything other than [yes] to run the LCM function. ').lower()
            if lcmUserInputInt != 'yes':
                print('\nLeast Common Multiple: ', lcm(lcmUserInputList))
                break
        choice = False
    elif choice == 4:
        gcfUserInputList = []
        gcfUserInputInt = False
        while type(gcfUserInputInt) is not int or gcfUserInputInt <= 0 or gcfUserInputInt > 2000006:
            try:
                gcfUserInputInt = int(input('\nChoose a positive integer less than 2,000,006: '))
                gcfUserInputList.append(gcfUserInputInt)
            except:
                print('\nPlease choose a positive integer less than 1,000,000,000,000.')
                gcfUserInputInt = False
            gcfUserInputInt = input('\nWould you like to choose another number for the GCF? Type anything other than [yes] to run the GCF function. ').lower()
            if gcfUserInputInt != 'yes':
                print('\nGreatest Common Factor: ', gcf(gcfUserInputList))
                break
        choice = False
    elif choice == 5:
        indexChoice = False
        radicandChoice = False
        while (indexChoice == False or radicandChoice == False) or (type(indexChoice) is not int) or (type(radicandChoice) is not float) or (indexChoice <= 0):
            try:
                indexChoice = int(input('\nType a positive integer for the INDEX of this radical: '))
                if indexChoice < 1:
                    print('\nPlease input a valid, positive integer.')
                    indexChoice = False
            except:
                print('\nPlease input a valid, positive integer.')
                indexChoice = False
            try:
                radicandChoice = float(input('\nType a positive, rational number for the RADICAND of this radical: '))
                if radicandChoice <= 0:
                    print('\nPlease input a valid, positive, rational number.')
                    radicandChoice = False
                elif radicandChoice < indexChoice:
                    print('\nThe RADICAND cannot be less than the INDEX.')
                    radicandChoice = False
            except:
                print('\nPlease input a valid, positive, rational number.')
                radicandChoice = False
        simplifiedRadical = simplifyRadical(indexChoice, radicandChoice)
        print('\nIndex: ', simplifiedRadical[0], '\nMultiplier: ', simplifiedRadical[1], '\nRadicand: ', simplifiedRadical[2])
        choice = False
    elif choice == 6:
        limitChoice = False
        while type(limitChoice) is not int or limitChoice <= 0:
            try:
                limitChoice = int(input('Choose the limit which all generated primes will be less than: '))
                if limitChoice <= 0:
                    print('Please choose a positive integer.')
                    limitChoice = False
            except:
                print('Please choose a positive integer.')
                limitChoice = False
        generateMorePrimes(limitChoice)
        print('Done.')
    again = input('\nWould you like to run another function? Type anything other than [yes] to end this program. ').lower()