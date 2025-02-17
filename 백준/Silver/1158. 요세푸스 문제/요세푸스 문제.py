n, k = map(int, input().split())
people = list(range(1, n + 1))
result = []
current = 0

while people:
    current = (current + k - 1) % len(people)
    result.append(people.pop(current))

print(f'<{", ".join(map(str, result))}>')