from collections import defaultdict, deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
family_tree = defaultdict(list)
indegree = defaultdict(int)
bloodline_score = defaultdict(float)

king_name = input().strip()
id_cnt = 1
name_id = {king_name: id_cnt}
bloodline_score[id_cnt] = 1.0

for _ in range(N):
    child_name, parent1_name, parent2_name = input().strip().split()
    if child_name not in name_id:
        id_cnt += 1
        name_id[child_name] = id_cnt

    if parent1_name not in name_id:
        id_cnt += 1
        name_id[parent1_name] = id_cnt

    if parent2_name not in name_id:
        id_cnt += 1
        name_id[parent2_name] = id_cnt

    child_id = name_id[child_name]
    parent1_id = name_id[parent1_name]
    parent2_id = name_id[parent2_name]

    family_tree[parent1_id].append(child_id)
    indegree[child_id] += 1
    family_tree[parent2_id].append(child_id)
    indegree[child_id] += 1

q = deque()
for i in range(1, id_cnt + 1):
    if indegree[i] == 0:
        q.append((i, bloodline_score[i]))

while q:
    parent_id, parent_score = q.popleft()

    for child_id in family_tree[parent_id]:
        indegree[child_id] -= 1
        bloodline_score[child_id] += parent_score / 2

        if indegree[child_id] == 0:
            q.append((child_id, bloodline_score[child_id]))

max_score = -1.0
closest_bloodline_name = ""

for _ in range(M):
    claimant_name = input().strip()
    id = name_id.get(claimant_name, 0)
    score = bloodline_score.get(id, 0)
    if score > max_score:
        max_score = score
        closest_bloodline_name = claimant_name

print(closest_bloodline_name)