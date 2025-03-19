import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
   x1, y1, r1, x2, y2, r2 = map(int, input().split())
   
   distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
   
   if distance == 0 and r1 == r2:
       print(-1)
   elif distance == abs(r1 - r2) or distance == r1 + r2:
       print(1)
   elif distance > r1 + r2 or distance < abs(r1 - r2):
       print(0)
   else:
       print(2)