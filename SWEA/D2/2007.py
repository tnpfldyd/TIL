import sys

sys.stdin = open("2007input.txt", "r")

T = int(input())
for i in range(1, T+1):
    a = input()
    
    result = 0
    for j in range(len(a)):
        if a[0] == a[1]:
            result += 1
            print('#'+str(i), result)
            break
        elif a[00] != a[1]:
            result += 1
            if a[0:result] == a[result:result+result]:
                print('#'+str(i), result)
                break
