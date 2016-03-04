from functools import reduce

# Super fast factor function modified to not find the number itself and 1,
# and also to return True if ther eare no factors, meaning it's prime 
def factors(n):    
    try: 
    	return set(reduce(list.__add__, 
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
    except TypeError:
    	return True
factorz = factors(600851475143)

# Print all the numbers and whether they're primes or not. Pick highest prime.
for fac in factorz:
	print(fac, factors(fac))