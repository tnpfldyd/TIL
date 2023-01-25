import itertools
def solution(users, emoticons):
    temp = [10, 20, 30, 40]
    person, result = 0, 0
    for i in itertools.product(temp, repeat=len(emoticons)):
        sign, total = 0, 0
        for user in users:
            dis, money = user
            cnt = 0
            for idx, j in enumerate(i):
                if j >= dis:
                    cnt += emoticons[idx] - (emoticons[idx] * j // 100)
            if cnt >= money:
                sign += 1
            else:
                total += cnt
        print(sign, total)
        if person < sign:
            person = sign
            result = total
        elif person == sign:
            if result < total:
                result = total
    return [person, result]
