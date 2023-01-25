import sys
input = sys.stdin.readline

N = int(input())
string_arr = []
for _ in range(N):
    string_arr.append(input().strip())
alpha_dic = {"A" : 0, "E" : 1, "I" : 2, "O" : 3, "U" : 4}
answer = 0

def dfs(word, bit):
    if bit == (1 << N) - 1:
        return 0
    last_alpha = alpha_dic[string_arr[word][-1]]
    if visited[last_alpha][bit] != -1:
        return visited[last_alpha][bit]
    ret = 0
    for i in range(N):
        if not (bit & 1 << i) and alpha_dic[string_arr[i][0]] == last_alpha:
            ret = max(ret, dfs(i, bit | 1 << i) + len(string_arr[i]))
    visited[last_alpha][bit] = ret
    return ret
for i in range(N):
    visited = [[-1] * (1 << N) for _ in range(5)]
    answer = max(answer, dfs(i, 1 << i) + len(string_arr[i]))
print(answer)
