def sieve(x):
  primes = dict()
  for i in range(2,x+1):
    primes[i] = True

  for i in primes:
    factors = range(i,x+1,i)
    for j in factors[1:]:
      primes[j] = False

  return [i for i in primes if primes[i] == True]

print sieve(1000000)[10000]