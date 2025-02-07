import sys
input = sys.stdin.readline

while True:
    n = int(input()) 
    if not n:
        break

    arr = []
    for _ in range(n):
        arr.append(int(input()))
    
    
    for i in range(1,n):
        arr[i] = max(arr[i-1] + arr[i], arr[i])

    print(max(arr))