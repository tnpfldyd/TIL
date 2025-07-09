import sys
input = sys.stdin.readline

X = int(input())

sticks = [64]

while sum(sticks) > X:
   sticks.sort()
   shortest = sticks.pop(0)
   half = shortest // 2
   
   if sum(sticks) + half >= X:
       sticks.append(half)
   else:
       sticks.append(half)
       sticks.append(half)

print(len(sticks))