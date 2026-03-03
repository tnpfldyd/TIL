import sys
input = sys.stdin.readline

B, C, D = map(int, input().split())
burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))

original = sum(burgers) + sum(sides) + sum(drinks)

burgers.sort(reverse=True)
sides.sort(reverse=True)
drinks.sort(reverse=True)

set_cnt = min(B, C, D)

discounted = 0
for i in range(set_cnt):
    discounted += (burgers[i] + sides[i] + drinks[i]) * 9 // 10

discounted += sum(burgers[set_cnt:]) + sum(sides[set_cnt:]) + sum(drinks[set_cnt:])

print(original)
print(discounted)