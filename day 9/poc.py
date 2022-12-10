ops = open("churro.txt", "r").read().splitlines()

OPERATOR = { 'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0) }

def move_the_rope(rope_length):
  visited = set()
  rope = [(0, 0) for _ in range(rope_length)]
  for op in ops:
    direction, steps = op.split(" ")
    for _ in range(int(steps)):
      # move the head
      rope[rope_length-1] = (
        rope[rope_length-1][0] + OPERATOR[direction][0],
        rope[rope_length-1][1] + OPERATOR[direction][1]
      )

      # move the rest of the knots
      for i in reversed(range(rope_length-1)):
        dx = rope[i+1][0] - rope[i][0]
        dy = rope[i+1][1] - rope[i][1]
        if abs(dx) > 1 or abs(dy) > 1:
          rope[i] = (
            rope[i][0] + (dx > 0) - (dx < 0),
            rope[i][1] + (dy > 0) - (dy < 0),
          )
        else:
          break

      visited.add(rope[0])
  return visited

print(len(move_the_rope(2)))
print(len(move_the_rope(10)))