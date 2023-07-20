MOD = int(1e9) + 7

N, L, R = map(int, input().split())

s = [[[0] * (R+1) for _ in range(L+1)] for _ in range(N+1)]


s[1][1][1] = 1

for i in range(2, N+1):
    for j in range(1, L+1):
        for k in range(1, R+1):
            s[i][j][k] = s[i-1][j][k] * (i-2) # i-1개의 빌딩 중 j,k 이하 높이중에서 i-2개의 빌딩을 선택하는 경우의 수
            s[i][j][k] += s[i-1][j][k-1] # i-1개의 빌딩 중 k-1개가 오른쪽에서 보이는 경우의 수
            s[i][j][k] += s[i-1][j-1][k] # i-1개의 빌딩 중 j-1개가 왼쪽에서 보이는 경우의 수
            s[i][j][k] %= MOD

print(s[N][L][R])