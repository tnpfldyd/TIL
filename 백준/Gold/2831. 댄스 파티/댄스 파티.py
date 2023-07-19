def count_dance(fos, neg):
    cnt = 0
    i = 0
    j = 0
    while i < len(fos) and j < len(neg):
        if fos[i] < neg[j]:
            cnt += 1
            i += 1
            j += 1
        else:
            i += 1

    return cnt


n = int(input())

malePos = []
malePeg = []
femalePos = []
femalePeg = []

for height in map(int, input().split()):
    if height > 0:
        malePos.append(height)
    else:
        malePeg.append(abs(height))

for height in map(int, input().split()):
    if height > 0:
        femalePos.append(height)
    else:
        femalePeg.append(abs(height))

malePos.sort(reverse=True)
malePeg.sort(reverse=True)
femalePos.sort(reverse=True)
femalePeg.sort(reverse=True)

result = count_dance(malePos, femalePeg)
result += count_dance(femalePos, malePeg)
print(result)