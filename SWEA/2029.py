import sys

sys.stdin = open("2029input.txt", "r")

a = int(input())

for i in range(1, a  + 1):
    b, c = map(int, input().split())
    print('#'+str(i), b // c, b % c)