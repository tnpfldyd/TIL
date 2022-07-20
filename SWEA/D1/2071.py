import sys

sys.stdin = open("2071input.txt", "r")

T = int(input())
for i in range(1, T +1):
    a = map(int, input().split())
    b = sum(a)/10
    print('#'+str(i),'%.0f'%b)