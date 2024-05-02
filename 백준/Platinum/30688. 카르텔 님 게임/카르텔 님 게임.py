N, K = map(int,input().split())
print('A and B win' if N - K - 1 <= K and N - K - 1 != 1 else 'C win')