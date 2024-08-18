N, X = map(int, input().split())
patties = [0] * 51
buns = [0] * 51
total_layers = [0] * 51

patties[0] = 1
buns[0] = 0
total_layers[0] = patties[0] + buns[0]

for i in range(1, N + 1):
    patties[i] = patties[i - 1] * 2 + 1
    buns[i] = buns[i - 1] * 2 + 2
    total_layers[i] = patties[i] + buns[i]

def count_eaten_patties(burger_level, eaten_count):
    if burger_level == 0:
        return 1
    if eaten_count == 1:
        return 0
    elif eaten_count == total_layers[burger_level - 1] + 1:
        return patties[burger_level - 1]
    elif eaten_count < total_layers[burger_level - 1] + 1:
        return count_eaten_patties(burger_level - 1, eaten_count - 1)
    elif eaten_count == total_layers[burger_level - 1] + 2:
        return patties[burger_level - 1] + 1
    elif eaten_count <= total_layers[burger_level - 1] * 2 + 2:
        return patties[burger_level - 1] + 1 + count_eaten_patties(burger_level - 1, eaten_count - total_layers[burger_level - 1] - 2)
    else:
        return patties[burger_level - 1] * 2 + 1

print(count_eaten_patties(N, X))