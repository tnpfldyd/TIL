sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
w, h = 0, 0
for a, b in sizes:
    if a > b:
        w = max(w, a)
        h = max(h, b)
    else:
        w = max(w, b)
        h = max(h, a)
print(w*h)