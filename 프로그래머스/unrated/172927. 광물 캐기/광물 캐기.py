def solution(picks, minerals):
    total = sum(picks) * 5
    if len(minerals) > total:
        minerals = minerals[:total]
    pick_cnt = [[0, 0, 0] for _ in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            pick_cnt[i // 5][0] += 1
        elif minerals[i] == "iron":
            pick_cnt[i // 5][1] += 1
        else:
            pick_cnt[i // 5][2] += 1
    pick_cnt = sorted(pick_cnt, key=lambda x : (-x[0], -x[1], -x[2]))
    answer = 0
    for m in pick_cnt:
        dia, iron, stone = m
        for p in range(len(picks)):
            if p == 0 and picks[p]:
                picks[p] -= 1
                answer += dia + iron + stone
                break
            elif p == 1 and picks[p]:
                picks[p] -= 1
                answer += 5 * dia + iron + stone
                break
            elif p == 2 and picks[p]:
                picks[p] -= 1
                answer += 25 * dia + 5 * iron + stone
                break
    return answer