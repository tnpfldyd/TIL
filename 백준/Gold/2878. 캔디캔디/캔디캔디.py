import sys
input = sys.stdin.readline

candy, friend = map(int, input().split())
want = dict()
want[0] = 0
for _ in range(friend):
    w = int(input())
    try:
        want[w] += 1
    except:
        want[w] = 1

want_key = sorted(list(want.keys()), reverse=True)
for i in range(len(want_key)-1):
    need = (want_key[i] - want_key[i+1])*want[want_key[i]]
    if candy >= need:
        candy -= need
        want[want_key[i+1]] += want.pop(want_key[i])
    else:
        _key = want_key[i] - candy//want[want_key[i]]
        pop_v = want.pop(want_key[i])
        try:
            want[_key] += pop_v
        except:
            want[_key] = pop_v

        want[_key] -= candy%pop_v
        try:
            want[_key-1] += candy%pop_v
        except:
            want[_key-1] = candy%pop_v
        break
        
answer = 0
for key in want.keys():
    answer += key*key*want[key]
    answer %= 18446744073709551616
print(answer)