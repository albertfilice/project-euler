def modu(x):
  for y in range(1,21):
    if x % y != 0:
      return False
  return True

z = 20
while modu(z) == False:
  z += 20

print "Answer: " + str(z)