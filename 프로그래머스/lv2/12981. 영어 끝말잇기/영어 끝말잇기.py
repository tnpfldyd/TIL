def solution(n, words):
    answer = []
    visit = set()
    last = words[0][0]
    for idx, word in enumerate(words, 1):
        if word not in visit and last == word[0]:
            visit.add(word)
            last = word[-1]
        else:
            result = idx // n
            order = idx % n
            if not order:
                order = n
            else:
                result += 1
            answer.append(order), answer.append(result)
            break
    if not answer:
        answer.append(0), answer.append(0)
    return answer