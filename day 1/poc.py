data = open("churro.txt", "r").read().split("\n\n")

calories = sorted([sum(map(int, chunk.split("\n"))) for chunk in data], reverse=True)[0]
print(calories)

# segunda parte
calories = sum(sorted([sum(map(int, chunk.split("\n"))) for chunk in data], reverse=True)[0:3])
print(calories)