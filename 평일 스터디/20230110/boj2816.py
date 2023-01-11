import sys
input = sys.stdin.readline
N = int(input())
channels = []
for _ in range(N):
    channels.append(input().strip())
i, j = channels.index('KBS1'), channels.index('KBS2')
if i > j: 
    j += 1
print('1'*i + '4'*i + '1'*j + '4'*(j-1))