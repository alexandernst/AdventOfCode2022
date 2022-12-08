import math

data = open("churro.txt", "r").read().splitlines()

trees = [[int(h) for h in line] for line in data]
trees_rotated = [*zip(*trees)]

best_scenic_score = 0
visible = (len(trees) * 2) + (len(trees[0]) * 2) - 4
for col in range(1, len(trees) - 1):
  for row in range(1, len(trees[0]) - 1):
    lines_of_sight = [
      trees_rotated[row][0:col][::-1], # up, inverted because we'll reuse it for the best scenic score
      trees_rotated[row][col+1:], # down
      trees[col][0:row][::-1], # left, inverted because we'll reuse it for the best scenic score
      trees[col][row+1:], # right
    ]

    if any(all(trees[col][row] > h for h in line_of_sight) for line_of_sight in lines_of_sight):
      visible += 1

    # segunda parte
    visibility_distances = [[h >= trees[col][row] for h in line_of_sight] for line_of_sight in lines_of_sight]
    current_best = math.prod([len(distance) if True not in distance else distance.index(True) + 1 for distance in visibility_distances])
    best_scenic_score = current_best if current_best > best_scenic_score else best_scenic_score

print(visible)
print(best_scenic_score)