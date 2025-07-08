import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
   line = list(map(int, input().split()))
   n = line[0]
   numbers = line[1:]
   
   total = 0
   for i in range(n):
       for j in range(i + 1, n):
           total += math.gcd(numbers[i], numbers[j])
   
   print(total)