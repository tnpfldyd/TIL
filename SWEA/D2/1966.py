import sys

sys.stdin = open("1966input.txt", "r")
T = int(input())
for i in range(1, T+1):
    N = int(input())
    R = list(map(int, input().split()))
    R.sort()
    print('#'+str(i), *R)