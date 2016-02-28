import math


""" I got this function from "http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python" """
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def main():
  a = 1
  b = 2
  
  while True:
    factorCount = 0
    a = a + b 
    b += 1
    z = 2
    if len(factors(a)) > 500:
      return str(a) + " has " + str(len(factors(a))) + " factors"
    z += 2
    # This function below was way too slow to figure it out
    # while z <= math.sqrt(a): 
    #   if a % z == 0:
    #     factorCount += 1
    #     if factorCount > 500:
    #        return str(a) + " has " + str(factorCount) + " factors!"
    #   z += 2

print main()

