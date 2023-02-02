def solution(chicken):
    cnt = 0
    while True:
        if chicken // 10 == 0:
            break
        temp = chicken // 10
        chicken -= (temp * 10)
        chicken += temp
        cnt += temp
    return cnt