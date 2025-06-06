from collections import Counter
import math

N = input()
counter = Counter(N)

six_nine = counter.get('6', 0) + counter.get('9', 0)
six_nine_sets = math.ceil(six_nine / 2)

max_others = max(
    counter.get(str(i), 0)
    for i in range(10)
    if i != 6 and i != 9
)

print(max(six_nine_sets, max_others))