import sys
input = sys.stdin.readline
N = int(input())
chanels = []
for _ in range(N):
    chanels.append(input().strip())
i, j = chanels.index('KBS1'), chanels.index('KBS2')
if i > j: 
    j += 1
print('1'*i + '4'*i + '1'*j + '4'*(j-1))