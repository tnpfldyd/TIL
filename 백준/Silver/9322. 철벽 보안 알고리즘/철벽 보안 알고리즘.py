import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    key1 = input().split()
    key2 = input().split()
    encrypted = input().split()
    mapping = [key1.index(word) for word in key2]
    result = [''] * n
    for i in range(n):
        result[mapping[i]] = encrypted[i]
    print(' '.join(result))