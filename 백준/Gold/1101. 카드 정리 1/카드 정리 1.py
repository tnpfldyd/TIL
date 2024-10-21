N, M = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]

joker_boxes = []
single_color_indices = []

for box in boxes:
    has_color = False
    single_color_index = -1
    for index in range(M):
        if box[index]:          
            if not has_color:
                has_color = True
                single_color_index = index
            else: 
                if single_color_index != -1:
                    joker_boxes.append(box)
                single_color_index = -1
    if single_color_index != -1:
        single_color_indices.append(single_color_index)

unique_single_colors = list(set(single_color_indices))
if len(joker_boxes) == 0:
    if len(single_color_indices) - len(unique_single_colors) > 0:
        print(len(single_color_indices) - len(unique_single_colors) - 1)
    else:
        print(len(single_color_indices) - len(unique_single_colors))
else:
    print(len(joker_boxes) - 1 + len(single_color_indices) - len(unique_single_colors))