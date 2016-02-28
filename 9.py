def main():
  for c in range(1,1001):
    for b in range(1,c):
      for a in range(1,b):
        asq = a**2
        bsq = b**2
        csq = c**2
        if asq + bsq == csq:
          if a + b + c == 1000:
            return a * b * c