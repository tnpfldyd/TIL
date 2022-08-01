import sys
input = sys.stdin.readline
T = int(input())
result = []
result2 = {}
for i in range(T):
    number = int(input())
    result.append(number)
    if number not in result2:
        result2[number] = 1
    else:
        result2[number] += 1
one = sum(result)/T
print(round(one))
two = sorted(result)
print(two[T//2])
three = sorted([k for k,v in result2.items() if max(result2.values()) == v])
if len(three) > 1:
    print(three[1])
else:
    print(*three)
four = max(result) - min(result)
print(four)