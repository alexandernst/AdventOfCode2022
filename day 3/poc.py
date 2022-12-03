from string import ascii_letters

data = open("churro.txt", "r").read().split("\n")

items = []
for item in data:
  l, r = item[:len(item)//2], item[len(item)//2:]
  common = list(set(l) & set(r))[0]
  items.append(ascii_letters.index(common) + 1)
print(sum(items))

# segunda parte
items = []
for n in range(0, len(data), 3):
  a, b, c = data[n:n+3]
  common = list(set(a) & set(b) & set(c))[0]
  items.append(ascii_letters.index(common) + 1)
print(sum(items))