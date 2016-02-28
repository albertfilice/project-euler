one_to_nine = ["one","two","three","four","five","six","seven","eight","nine"]
ten_to_nineteen = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
twenty_to_ninety = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def one_to_onehundred():
  count = 0
  for x in range(10):
    if x == 0:
      for y in range(9):
        count += len(one_to_nine[y])
    elif x == 1:
      for y in range(10):
        count += len(ten_to_nineteen[y])
    else:
      count += len(twenty_to_ninety[x-2])
      for y in range(9):
        count += len(twenty_to_ninety[x-2])
        count += len(one_to_nine[y])
  return count

def onehundred_to_onethousand():
  count = 0
  for x in range(9):
    count += len(one_to_nine[x]) + 7
    for y in range(9):
      count += len(one_to_nine[x]) + 10 + len(one_to_nine[y])
    for y in range(10):
      count += len(one_to_nine[x]) + 10 + len(ten_to_nineteen[y])
    for y in range(8):
      count += len(one_to_nine[x]) + 10 + len(twenty_to_ninety[y])
      for z in range(9):
        count += len(one_to_nine[x]) + 10 + len(twenty_to_ninety[y]) + len(one_to_nine[z])
  return count

print one_to_onehundred() + onehundred_to_onethousand() + len("onethousand")