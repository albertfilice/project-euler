def collatz(n):
  counter = [n]
  while n > 1:
    if n % 2 == 0:
      n = n/2
    else:
      n = (3 * n) + 1
    counter.append(n)
  return counter

def largest_collatz_under_1mil():
  largest = 0
  largest_num = 0
  for x in range(1,1000000):
    temp = len(collatz(x))
    if int(temp) > int(largest):
      # print str(temp) + " is bigger than " + str(largest)
      largest = temp
      largest_num = x

  return "largest string was " + str(largest) + " by the number " + str(largest_num)

print (largest_collatz_under_1mil())