rocks = set()
for line in open("churro.txt", "r").read().splitlines():
  coords = list(map(eval, line.split(" -> ")))
  for i in range(len(coords) - 1):
    x1, y1 = coords[i]
    x2, y2 = coords[i + 1]
    # bresenham... you're not welcome in this aoc...
    if x1 == x2: # horizontal
      points = [(x1, i) for i in range(y1, y2, int(abs(y2-y1) / (y2-y1)))]
    else:        # vertical
      points = [(i, y1) for i in range(x1, x2, int(abs(x2-x1) / (x2-x1)))]
    rocks.update([*points, (x2, y2)])
xs, ys = sorted(x for x, _ in rocks), sorted(y for _, y in rocks)

def drop(sx, sy, ey, rocks, sand):
  _next = [(sx, sy+1), (sx-1, sy+1), (sx+1, sy+1)]
  points = [point for point in _next if point not in rocks and point not in sand]
  if len(points) == 0:
    return (sx, sy)
  elif points[0][1] > ey:
    return (0, 0) # sand is free-falling forever
  return drop(*points[0], ey, rocks, sand)

sand = set()
point = drop(500, 0, ys[-1], rocks, sand)
while point != (0, 0) and point != (500, 0):
  sand.add(point)
  point = drop(500, 0, ys[-1], rocks, sand)
print(len(sand))

# segunda parte
sand = set()
rocks.update([(x, ys[-1] + 2) for x in range(-(xs[-1] * ys[-1]), xs[-1] * ys[-1])])
xs, ys = sorted(x for x, _ in rocks), sorted(y for _, y in rocks)

point = drop(500, 0, ys[-1], rocks, sand)
while point != (0, 0) and point != (500, 0):
  sand.add(point)
  point = drop(500, 0, ys[-1], rocks, sand)
sand.add((500, 0))
print(len(sand))

"""
for y in range(ys[0] - 3, ys[-1] + 3):
  for x in range(xs[0] - 3, xs[-1] + 3):
    point = (x, y)
    if point in rocks:
      print("#", end="")
    elif point in sand:
      print("o", end="")
    else:
      print(".", end="")
  print("")
"""