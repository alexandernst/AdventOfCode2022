import re
from collections import defaultdict

crates, ops = open("churro.txt", "r").read().split("\n\n")

cratemap = defaultdict(list)
for line in crates.split("\n")[:-1]:
  for idx, char in enumerate([line[i] for i in range(1, len(line), 4)]):
    if not char == " ": cratemap[idx+1].append(char)

cratemap1 = cratemap.copy()
for line in ops.split("\n"):
  n, src, dst = map(int, re.findall(r"move (\d+) from (\d+) to (\d+)", line)[0])
  cratemap1[dst] = cratemap1[src][:n][::-1] + cratemap1[dst]
  cratemap1[src] = cratemap1[src][n:]
print("".join([cratemap1[i][0] for i in range(1, len(cratemap1.keys()) + 1)]))

# segunda parte
cratemap2 = cratemap.copy()
for line in ops.split("\n"):
  n, src, dst = map(int, re.findall(r"move (\d+) from (\d+) to (\d+)", line)[0])
  cratemap2[dst] = cratemap2[src][:n] + cratemap2[dst]
  cratemap2[src] = cratemap2[src][n:]
print("".join([cratemap2[i][0] for i in range(1, len(cratemap2.keys()) + 1)]))