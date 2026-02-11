import sys
input = sys.stdin.readline

yeon_name = input().strip()
teams = sorted([input().strip() for _ in range(int(input()))])

def calc_prob(team):
    s = yeon_name + team
    L, O, V, E = [s.count(c) for c in 'LOVE']
    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

print(max(teams, key=calc_prob))
