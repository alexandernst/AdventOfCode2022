ops = open("churro.txt", "r").read().splitlines()

CYCLE = 0
X = 1
OP_COST = { "addx": 2, "noop": 1 }
BREAKPOINTS = [20, 60, 100, 140, 180, 220]
BREAKPOINT_VALUES = []
FB = [_ for _ in range(40 * 6)]

for op in ops:
  instruction = op.split(" ")
  for tick in range(OP_COST[instruction[0]]):
    FB[CYCLE] = "#" if (CYCLE) % 40 in [X - 1, X, X + 1] else " "
    CYCLE += 1
    if CYCLE in BREAKPOINTS:
      BREAKPOINT_VALUES.append(X)
  if instruction[0] == "addx":
    X = X + int(instruction[1])

print(sum([a * b for a, b in zip(BREAKPOINTS, BREAKPOINT_VALUES)]))
for i in range(0, len(FB), 40): print("".join(FB[i:i + 40]))