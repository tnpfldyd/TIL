import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

round_num = 1

while True:
    if abs(a - b) == 1 and min(a, b) % 2 == 1:
        print(round_num)
        break
    
    a = (a + 1) // 2
    b = (b + 1) // 2
    
    if a == b:
        print(-1)
        break
    
    round_num += 1