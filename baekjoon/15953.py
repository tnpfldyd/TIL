import sys
input = sys.stdin.readline
def score1(a):
    if a == 1:
        return 5000000
    elif 4 > a > 1:
        return 3000000
    elif 7 > a >= 4:
        return 2000000
    elif 11 > a >= 7:
        return 500000
    elif 16 > a >= 11:
        return 300000
    elif 22 > a >= 16:
        return 100000
    else:
        return 0
def score2(b):
    if b == 1:
        return 5120000
    elif 4 > b > 1:
        return 2560000
    elif 8 > b >= 4:
        return 1280000
    elif 16 > b >= 8:
        return 640000
    elif 32 > b >= 16:
        return 320000
    else:
        return 0
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(score1(a) + score2(b))