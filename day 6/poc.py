msg = open("churro.txt", "r").read()

marker = []
for idx, char in enumerate(msg):
  marker = [*marker, char][-4:]
  if len(set(marker)) == 4: break
print(idx+1)

# segunda parte
marker = []
for idx, char in enumerate(msg):
  marker = [*marker, char][-14:]
  if len(set(marker)) == 14: break
print(idx+1)