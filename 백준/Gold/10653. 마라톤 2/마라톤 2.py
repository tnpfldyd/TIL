import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    input = sys.stdin.readline
    
    N, K = map(int, input().split())
    points = []
    dp = [[-1] * N for _ in range(K + 1)]

    for i in range(N):
        x, y = map(int, input().split())
        points.append(Point(x, y))

    dp[0][0] = 0

    for i in range(1, N):
        for j in range(K + 1):
            if i - j > 0:
                min_distance = float('inf')
                for k in range(j + 1):
                    temp = dp[j - k][i - k - 1]
                    if temp == -1:
                        continue
                    distance = abs(points[i - k - 1].x - points[i].x) + abs(points[i - k - 1].y - points[i].y)
                    min_distance = min(min_distance, temp + distance)
                dp[j][i] = min_distance

    result = dp[0][N - 1]
    for i in range(1, K + 1):
        result = min(result, dp[i][N - 1])

    print(result)

if __name__ == "__main__":
    main()