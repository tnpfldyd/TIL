import sys
input = sys.stdin.readline

members = []
for _ in range(3):
    p, y, s = input().split()
    members.append((int(p), int(y), s))

years = sorted([y % 100 for _, y, _ in members])
team1 = "".join(f"{yy:02d}" for yy in years)

members_sorted = sorted(members, key=lambda x: x[0], reverse=True)
team2 = "".join(s[0] for _, _, s in members_sorted)

print(team1)
print(team2)