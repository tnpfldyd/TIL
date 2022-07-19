import sys

sys.stdin = open("2070input.txt", "r")

T = int(input())

for i in range(1, T + 1):
    a, b = map(int, input().split())
    if a > b :
        print('#'+str(i), '>')
    elif a == b:
        print('#'+str(i), '=')
    else:
        print('#'+str(i), '<')
