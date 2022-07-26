a, b = map(int, input().split())
c = int(input())
Time = b + c
while True:
    if Time >= 60:
        Time -= 60
        a += 1
    if a >= 24:
        a -= 24
    if a < 24 and Time < 60:
        print(a, Time)
        break