T = int(input())
cnt = 1
rule = 6
result = 1
while True:
    if T == 1:
        print(1)
        break
    elif T > result + cnt * rule:
        result += cnt * rule
        cnt += 1
    else:
        print(cnt + 1)
        break