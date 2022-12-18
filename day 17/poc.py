from itertools import cycle
from shapely import Polygon
from shapely.ops import unary_union
from shapely.affinity import translate

JETS = list(open("churro.txt", "r").read())
SHAPES = [
  [(0, 0), (0, 1), (1, 1), (4, 1), (4, 0), (0, 0)], # -
  [(1, 0), (1, 1), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (2, 1), (2, 0), (1, 0)], # +
  [(0, 0), (0, 1), (2, 1), (2, 3), (3, 3), (3, 0), (0, 0)], # ⅃
  [(0, 0), (0, 4), (1, 4), (1, 0), (0, 0)], # |
  [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)], # □
]
FLOOR = [(0, 0), (7, 0), (7, -1), (0, -1), (0, 0)] # _______

def throw_shapes(n):
  jets = cycle(range(len(JETS)))
  shapes = cycle(range(len(SHAPES)))
  floor = Polygon(FLOOR)

  for iteration in range(n):
    _, _, _, height = floor.bounds
    shape = Polygon(SHAPES[next(shapes)])
    shape = translate(shape, xoff=2, yoff=height + 3)

    falling = True
    while falling:
      jet = JETS[next(jets)]

      minx, _, maxx, _ = shape.bounds
      next_pos = translate(shape, xoff= -1 if jet == "<" else 1)
      intersection = floor.intersection(next_pos)
      if (jet == "<" and minx > 0 and (intersection.is_empty or intersection.area == 0)):
        shape = next_pos
      elif (jet == ">" and maxx < 7 and (intersection.is_empty or intersection.area == 0)):
        shape = next_pos

      next_pos = translate(shape, yoff=-1)
      intersection = floor.intersection(next_pos)
      if intersection.is_empty or intersection.area == 0:
        shape = next_pos
      else:
        falling = False

    floor = unary_union([floor, shape])

    # sweep the floor every 30 shapes
    if iteration > 0 and iteration % 30 == 0:
      eraser = Polygon([(0, -1), (0, height - 50), (7, height - 50), (7, -1)])
      floor = floor.difference(eraser)

  _, _, _, height = floor.bounds
  return height, floor

height, floor = throw_shapes(2022)
print(int(height))

#height, floor = throw_shapes(1000000000000)
#print(int(height))

#import matplotlib.pyplot as plt
#import geopandas as gpd
#_, _, _, height = floor.bounds
#pol = Polygon([(0, 0), (0, height), (height, 10), (10, 0), (0, 0)])
#pol = pol.difference(floor)
#myPoly = gpd.GeoSeries(floor)
#myPoly.plot()
#plt.show()