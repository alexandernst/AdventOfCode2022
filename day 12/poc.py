from string import ascii_letters

grid = [list(line) for line in open("churro.txt", "r").read().splitlines()]
heights = { char: pos for pos, char in enumerate(ascii_letters[:26]) }
heights.update({ "S": 0, "E": 25 })
width = len(grid[0])
height = len(grid)

def bfs(start, target):
  path = []
  queue = [(start, [])]
  visited = set(start)
  while queue:
    (x, y), path = queue.pop(0)
    if (x, y) == target: return path

    for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
      new_node = (x2, y2)
      if (
        0 <= x2 < width and # can we go left / right?
        0 <= y2 < height and # can we go up / down?
        new_node not in visited and # have we already been there?
        heights[grid[y2][x2]] <= heights[grid[y][x]] + 1 # can we climb it?
      ):
        queue.append((new_node, path + [new_node]))
        visited.add(new_node)

  return []

starts = []
for i, row in enumerate(grid):
  for j, col in enumerate(row):
    if col == "S": start = (j, i)
    if col == "E": target = (j, i)
    if col == "a": starts.append((j, i))
path = bfs(start, target)
print(len(path))

# segunda parte
print(min([len(path) for path in [bfs(start, target) for start in starts] if len(path) > 0]))

# debug
"""
from pprint import pprint
for row in range(height):
  for col in range(width):
    if (col, row) in path:
      idx = path.index((col, row))
      if idx + 1 < len(path):
        next = path[idx + 1]
        if next[0] > col:
          print(">", end="")
        elif next[0] < col:
          print("<", end="")
        elif next[1] > row:
          print("v", end="")
        elif next[1] < row:
          print("^", end="")
      else:
        print("E", end="")
    else:
      print(".", end="")
  print("")
"""