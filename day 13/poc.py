from functools import cmp_to_key

data = open("churro.txt", "r").read()

cast = lambda n: [n] if type(n) == int else n

def compare(left, right):
  if type(left) == int and type(right) == int:
    return (left > right) - (left < right)
  elif type(left) == int or type(right) == int:
    return compare(cast(left), cast(right))

  for cross_left, cross_right in zip(left, right):
    res = compare(cross_left, cross_right)
    if res: return res

  return compare(len(left), len(right))

indices_right_order = []
for idx, pairs in enumerate(data.split("\n\n")):
  left, right = map(eval, pairs.split("\n"))
  indices_right_order += [idx + 1] if compare(left, right) == -1 else []
print(sum(indices_right_order))

# segunda parte
all_packets = [*list(map(eval, data.replace("\n\n", "\n").split("\n"))), [[2]], [[6]]]
sorted_packets = sorted(all_packets, key=cmp_to_key(compare))
print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))