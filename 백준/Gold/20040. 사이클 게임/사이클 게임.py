import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def main():
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return True
        parent[x] = y
        return False

    N, M = map(int, input().split())
    parent = [i for i in range(N)]
    answer = 0
    for i in range(1, M + 1):
        a, b = map(int, input().split())
        if union(a, b):
            answer = i
            break
    print(answer)
if __name__ == "__main__":
    main()