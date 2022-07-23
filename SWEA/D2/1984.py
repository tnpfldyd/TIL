import sys

sys.stdin = open("1984input.txt", "r")
T = int(input())

for i in range(1, T+1):
    a = list(map(int, input().split()))
    a.sort()
    b = (sum(a[1:9]))/8
    print('#'+str(i), '%.0f' %b)