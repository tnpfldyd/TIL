T = int(input())
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    T -= a * b
print('Yes' if T == 0 else 'No')