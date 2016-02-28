def sieve(x):
    primes = dict()
    for i in range(1,x+1,2):
        primes[i] = True

    for i in primes:
        factors = range(i,x+1,i)
        for j in factors[1:]:
            primes[j] = False

    return [i for i in primes if primes[i] == True]

primes_below_max = sieve(1000)
print(primes_below_max)
# print(max(primes_below_max))