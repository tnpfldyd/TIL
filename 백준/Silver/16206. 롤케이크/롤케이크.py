n, m = map(int, input().split())
cakes = list(map(int, input().split()))

multiples = []
others = []

for a in cakes:
    if a % 10 == 0:
        multiples.append(a)
    else:
        others.append(a)

multiples.sort()
others.sort()
answer = 0

for a in multiples:
    pieces = a // 10
    cuts_needed = pieces - 1

    if m >= cuts_needed:
        m -= cuts_needed
        answer += pieces
    else:
        answer += m
        m = 0
        break

for a in others:
    if m == 0:
        break

    pieces = a // 10
    cuts_needed = pieces

    if m >= cuts_needed:
        m -= cuts_needed
        answer += pieces
    else:
        answer += m
        m = 0
        break

print(answer)