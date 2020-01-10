def findPrime(number):
    if 2 == number or 3 == number:
        return True
    startnum = 2
    while startnum <= number / startnum:
        if number % startnum == 0:
            return False
        startnum = startnum + 1

    return True


def listprime(number):
    return [v for v in range(2, number) if findPrime(v)]


primes = listprime(100)

print(primes)
print(len(primes))




