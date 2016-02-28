def largest_palindrome_product():
  longlist = []
  for x in range(100,1000):
    for y in range(100,1000):
      temp = str(x*y)
      if len(temp) % 2 == 0:
        if is_palindrome(temp) == True:
          longlist.append(int(temp))
  return max(longlist)

def is_palindrome(num):
  for x in range(0,(len(num)/2)):
    if num[x] != num[(len(num) - 1) - x]:
      return False
  return True



print largest_palindrome_product()