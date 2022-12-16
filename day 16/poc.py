import re

valves = {}
for line in open("churro.txt", "r").read().splitlines():
  valve, rate, tunnels = re.findall(r"Valve (.*?) .*=(\d*).*valves? (.*)", line)[0]
  valves[valve] = {
    "flow_rate": int(rate),
    "tunnels": tunnels.split(", "),
    "paths": {},
  }

def bfs(queue, end):
  depth = 1
  while True:
    new_queue = set()
    for valve in queue:
      if valve == end: return depth
      new_queue.update(valves[valve]["tunnels"])
    queue = new_queue
    depth += 1

for kvalve, vvalve in valves.items():
  for valvename in list(valves.keys())[1:]:
    if kvalve == valvename or valves[valvename]["flow_rate"] == 0: continue
    vvalve["paths"][valvename] = bfs(vvalve["tunnels"], valvename)


def find_best_score(opened, released_pressure, kvalve, minutes_left):
  if minutes_left <= 0: return released_pressure

  scores = []
  valve = valves[kvalve]

  if kvalve in opened:
    paths = valve["paths"]
    for target in [target for target in paths.keys() if target not in opened]:
      score = find_best_score(opened, released_pressure, target, minutes_left - paths[target])
      scores.append(score)
  else:
    new_released_pressure = released_pressure + valve["flow_rate"] * minutes_left
    score = find_best_score(set([*opened, kvalve]), new_released_pressure, kvalve, minutes_left - 1)
    scores.append(score)

  return max([released_pressure, *scores])

score = find_best_score(set(['AA']), 0, 'AA', 29)
print(score)