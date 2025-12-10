import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    j, N = map(int, input().split())
    areas = [r * c for r, c in (map(int, input().split()) for _ in range(N))]
    areas.sort() 

    box_count = 0 

    while j > 0 and areas:
        j -= areas.pop()
        box_count += 1

    print(box_count)