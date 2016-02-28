def sum_square_100():
  sum_square = 0
  for x in range(1,101):
    sum_square += x**2
  return sum_square

def square_sum_100():
  square_sum = 0
  for x in range(1,101):
    square_sum += x
  return square_sum**2

def difference_square_sum_and_sum_square(square_of_sum, sum_of_square):
  return square_of_sum - sum_of_square

print difference_square_sum_and_sum_square(square_sum_100(),sum_square_100())