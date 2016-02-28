def power_two(x):
  return 2**x

def sum_didgets(y):
  summation = 0
  for x in y:
    summation += int(x)
  return summation

print sum_didgets(str(power_two(1000)))