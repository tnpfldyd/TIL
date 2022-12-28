def solution(sizes):
    w, h = 0, 0
    for a, b in sizes:
        if a > b:
            w = max(w, a)
            h = max(h, b)
        else:
            w = max(w, b)
            h = max(h, a)
    return w*h