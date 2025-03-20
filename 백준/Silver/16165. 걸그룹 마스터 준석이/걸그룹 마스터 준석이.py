import sys
input = sys.stdin.readline

N, M = map(int, input().split())
team_to_members = {}
member_to_team = {}
for _ in range(N):
    team_name = input().strip()
    member_count = int(input())
    members = []
    for _ in range(member_count):
        member = input().strip()
        members.append(member)
        member_to_team[member] = team_name
    team_to_members[team_name] = sorted(members)
for _ in range(M):
    quiz_input = input().strip()
    quiz_type = int(input())
    if quiz_type == 0:
        for member in team_to_members[quiz_input]:
            print(member)
    elif quiz_type == 1:
        print(member_to_team[quiz_input])