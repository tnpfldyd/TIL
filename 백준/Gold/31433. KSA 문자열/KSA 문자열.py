KSA = "KSA"
def cal(target_string):
    idx = 0
    count = 0
    for char in target_string:
        if char == KSA[idx % 3]:
            idx += 1
        else:
            count += 1
    count += abs(idx - len(X))
    return count

X = input().strip()
answer = float('inf')

answer = min(answer, cal(X))
answer = min(answer, cal("K" + X))
answer = min(answer, cal("KS" + X))

print(answer)
