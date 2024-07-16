a, b = map(int, input().split())

def calc(number):
  if not number:
    return 0
  elif number == 1:
    return 1 
  elif not number % 2:
    return number // 2 + 2 * calc(number // 2)
  else:
    return number // 2 + 2 * calc(number // 2) + 1

print(calc(b) - calc(a-1))