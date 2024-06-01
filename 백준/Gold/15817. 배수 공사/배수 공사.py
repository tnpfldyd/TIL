import sys
input = sys.stdin.readline
def main():
    N, X = map(int, input().split())
    dist = [0] * 10001
    dist[0] = 1

    for _ in range(N):
        l, c = map(int, input().split())

        for i in range(X, 0, -1):
            temp = 0
            for j in range(c):
                temp += l
                if i - temp < 0:
                    break
                dist[i] += dist[i - temp]

    print(dist[X])

if __name__ == "__main__":
    main()
