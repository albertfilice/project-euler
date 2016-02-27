fibi = [1,2]
count1 = 0
count2 = 1
while fibi[count2] < 4000000:
  fibi.append(fibi[count1] + fibi[count2])
  count1 += 1
  count2 += 1
  print fibi
  print sum(fibi)

print fibi

fibi_sum = 0
for x in fibi:
  if x % 2 == 0:
    fibi_sum += x

print "X: " + str(fibi_sum)