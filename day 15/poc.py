import re
from shapely import Polygon, difference

sensors = []
beacons = set()

minx = 0
maxx = 0
for line in open("churro.txt", "r").read().splitlines():
  sx, sy, bx, by = list(map(int, re.findall(r"-?[0-9]+", line)))
  md = abs(sx - bx) + abs(sy - by)

  sensors.append({
    "p": (sx, sy),
    "md": md,
    "b": (bx, by),
  })
  beacons.add((bx, by))

  minx = min([minx, sx - md])
  maxx = max([maxx, sx + md + 1])

impossible = 0
y = 2000000
for x in range(minx, maxx):
  if (x, y) in beacons: continue
  for sensor in sensors:
    if (abs(x - sensor["p"][0]) + abs(y - sensor["p"][1])) <= sensor["md"]:
      impossible += 1
      break
print(impossible)

# segunda parte
polygons = []
limit = 4000000
limit_polygon = Polygon(((0, 0), (0, limit), (limit, limit), (limit, 0)))
for sensor in sensors:
  x, y = sensor["p"]
  md = sensor["md"]
  poly = Polygon(((x + md, y), (x, y + md), (x - md, y), (x, y - md)))
  polygons.append(poly)

diff = limit_polygon                          # "beacon" will be a polygon like
for polygon in polygons:                      # this. Get the center (beacon)
  diff = difference(diff, polygon)            #
beacon = diff.centroid                        #        / \
print(int(beacon.x) * limit + int(beacon.y))  #        \ /