import sys
input = sys.stdin.readline
N = int(input())
A = sorted(map(int, input().rstrip().split()))
if N == 1:
    print(1)
elif A[-1] <= sum(A[:N-1])+1:
    print(sum(A))
else:
    print(sum(A[:N-1])*2+1)