N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    dice.sort()
    print(sum(dice[:5]))
else:
    dice_min = [min(dice[i], dice[5 - i]) for i in range(3)]
    dice_min.sort()

    corner = dice_min[0] + dice_min[1] + dice_min[2]
    edge = dice_min[0] + dice_min[1]
    face = dice_min[0]

    corners = 4
    edges = (N - 2) * 4 * 2 + 4
    faces = (N - 2) * (N - 2) * 5 + (N - 2) * 4

    print(corner * corners + edge * edges + face * faces)