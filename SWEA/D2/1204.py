import sys

sys.stdin = open("1204input.txt", "r")
T = int(input())
for i in range(T):
    A = input()
    G = list(map(int, input().split()))
    F = {}
    for j in G:
        if j not in F:
            F[j] = 0
        F[j] += 1
    max_F = max(F , key = F.get) # 벨류가 제일 높은 키 찾는 코드
    print('#'+A, max_F)