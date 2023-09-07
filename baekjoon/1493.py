import sys
input = sys.stdin.readline

length, width, height = map(int, input().split())
volume = length * width * height
N = int(input())
cubes = [tuple(map(int, input().split())) for _ in range(N)]
cubes.sort(reverse=True)

answer, current = 0, 0

for idx, cnt in cubes:
    current *= 8 # 부피
    len = 2**idx
    limit = (length // len) * (width // len) * (height // len) - current
    limit = min(cnt, limit)
    answer += limit
    current += limit

print(answer if volume == current else -1)