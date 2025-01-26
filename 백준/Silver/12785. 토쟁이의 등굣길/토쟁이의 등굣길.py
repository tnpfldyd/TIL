from math import comb

w, h = map(lambda x: int(x) - 1, input().split())
x, y = map(lambda x: int(x) - 1, input().split())

to_toast = comb(x + y, y)
toast_to_school = comb(w - x + h - y, h - y)

print((to_toast * toast_to_school) % 1000007)