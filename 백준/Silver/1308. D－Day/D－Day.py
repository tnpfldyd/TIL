from datetime import date

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if y2 > y1 + 1000 or (y2 == y1 + 1000 and (m2 > m1 or (m2 == m1 and d2 >= d1))):
    print("gg")
else:
    d1 = date(y1, m1, d1)
    d2 = date(y2, m2, d2)
    print(f"D-{(d2 - d1).days}")