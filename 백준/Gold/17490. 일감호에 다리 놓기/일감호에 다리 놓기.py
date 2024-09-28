import sys

input = sys.stdin.readline
INF = 987654321

def main():
    N, M, K = map(int, input().split())
    cost = list(map(int, input().split()))
    v = []
    for _ in range(M):
        a, b = map(int, input().split())
        if a > b and a != N:
            a, b = b, a
        v.append((a-1, b-1))
    
    if M <= 1:
        print("YES")
        return
    
    v.sort()
    
    sum_cost = 0
    last = 0
    for i in range(len(v)):
        min_cost = INF
        left, right = v[i]
        for j in range(last, left + 1):
            min_cost = min(min_cost, cost[j])
        
        if last == 0 and v[-1][1] != 0:
            end = v[-1][1]
            for j in range(N - 1, end - 1, -1):
                min_cost = min(min_cost, cost[j])
        
        sum_cost += min_cost
        last = right
    
    if sum_cost <= K:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()