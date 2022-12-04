data = open("churro.txt", "r").read()

pairs_of_ranges = []
for group in data.split("\n"):
  pairs = [pair for pair in group.split(",")]
  ranges = [list(map(int, _range.split("-"))) for _range in pairs]
  pairs_of_ranges.append(ranges)

def issubset(a, b):
  return a[0] >= b[0] and a[1] <= b[1]

contained = [1 for a, b in pairs_of_ranges if issubset(a, b) or issubset(b, a)]
print(sum(contained))

# segunda parte
def overlap(a, b):
  return a[0] >= b[0] and a[0] <= b[1]

overlaped = [1 for a, b in pairs_of_ranges if overlap(a, b) or overlap(b, a)]
print(sum(overlaped))