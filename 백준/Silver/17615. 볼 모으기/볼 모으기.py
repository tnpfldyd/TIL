import sys
input = sys.stdin.readline

N = int(input())
balls = input().strip()

answer = min(
    balls.lstrip('R').count('R'),
    balls.rstrip('R').count('R'),
    balls.lstrip('B').count('B'),
    balls.rstrip('B').count('B')
)

print(answer)
