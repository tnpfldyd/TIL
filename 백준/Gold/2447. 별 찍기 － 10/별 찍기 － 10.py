def printStar(n):
  if n == 1:
    return ['*']

  cols = printStar(n // 3)
  
  row = []

  for col in cols:
    row.append(col * 3)
  for col in cols:
    row.append(col + ' ' * (n // 3) + col)
  for col in cols:
    row.append(col * 3)

  return row

N = int(input())

print('\n'.join(printStar(N)))