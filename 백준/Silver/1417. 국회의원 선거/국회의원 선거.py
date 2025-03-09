import sys
input = sys.stdin.readline

N = int(input())
votes = []
for i in range(N):
    votes.append(int(input()))

dasom_votes = votes[0]
other_votes = votes[1:]
bribe_count = 0

while True:
    if len(other_votes) == 0 or dasom_votes > max(other_votes):
        break
    
    max_votes_idx = other_votes.index(max(other_votes))
    other_votes[max_votes_idx] -= 1
    dasom_votes += 1
    bribe_count += 1

print(bribe_count)