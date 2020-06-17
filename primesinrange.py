# primes in range
import math
primes = []
possprime = []

def generateprimes(min, max):
    if min < 0 or not type(min) is int or max < 0 or not type(max) is int:
        print("Neither argument can be negative and must be integers.")
    elif max > 50000:
        print("Sorry, but that's just too much work.")
    else:
        primes.append(2)
        primes.append(3)
        x = 4
        while x <= max:
            b = 0
            while primes[b] < math.sqrt(x): # while b < len(primes):
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
            x += 1
        c = 0
        while primes[c] < min:
            c += 1
        return primes[c:]
print(generateprimes(0, 10000))
