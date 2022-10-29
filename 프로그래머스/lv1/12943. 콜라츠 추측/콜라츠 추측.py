def solution(num):
    cnt = 0
    answer = True
    while num != 1 and answer:
        cnt += 1
        if num % 2:
            num = (num*3) + 1
        else:
            num //= 2
        if cnt > 500:
            answer = False
    if answer:
        return cnt
    else:
        return -1 