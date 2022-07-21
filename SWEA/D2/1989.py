T = int(input())
for i in range(1, T+1):
    a = list(input())
    if a[0:] == a[::-1]:
        print('#'+str(i), '1')
    else:
        print('#'+str(i), '0')
