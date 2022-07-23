import sys

sys.stdin = open("1983input.txt", "r")
T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for i in range(1, T+1):
    a, k = map(int, input().split())
    result = []
    for j in range(a):
        b, c, d = map(int, input().split())
        e = (b * 0.35) + (c * 0.45) + (d * 0.20)
        result.append(e)
    kk = result[k-1]
    result.sort(reverse=True)
    N = a//10
    kgrade = result.index(kk) // N
    print('#'+str(i), grade[kgrade])