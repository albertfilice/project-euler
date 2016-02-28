def factorial(x):
  fac = 1
  for x in range(1,x+1):
    fac *= x
  return fac

def sum_didgets(y):
  summation = 0
  for x in y:
    summation += int(x)
  return summation

print sum_didgets(str(factorial(100)))