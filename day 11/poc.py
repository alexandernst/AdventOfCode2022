import math, copy

monkeys = []
for monkey in open("churro.txt", "r").read().split("\n\n"):
  monkey_data = monkey.splitlines()
  monkeys.append({
    "items": monkey_data[1].split(": ")[1].split(", "),
    "op": monkey_data[2].split("= ")[1],
    "test": int(monkey_data[3].split(" ")[-1:][0]),
    "true": int(monkey_data[4].split(" ")[-1:][0]),
    "false": int(monkey_data[5].split(" ")[-1:][0]),
    "n_inspections": 0,
  })

# Basically, the new_worry_level is getting too big to calculate the modulo for
# each monkey's "test" digit. We can make the entire operation faster if we
# calculate in advance the least common multiple (LCM) of the "test" digit of
# all monkeys, which is the product of all of them.
LCM = math.prod(monkey["test"] for monkey in monkeys)

def let_the_monkeys_do_simian_shenanigans(rounds, relief):
  _monkeys = copy.deepcopy(monkeys)
  for _ in range(rounds):
    for monkey in _monkeys:
      while len(monkey["items"]) and (item := monkey["items"].pop(0)):
        new_worry_level = eval(monkey["op"].replace("old", item)) # inspect
        new_worry_level = relief(new_worry_level) # calc reliefe
        target = monkey["true"] if new_worry_level % monkey["test"] == 0 else monkey["false"] # test
        _monkeys[target]["items"].append(str(new_worry_level)) # throw to new monkey
        monkey["n_inspections"] += 1

  return sorted(_monkeys, key=lambda monkey: monkey["n_inspections"])[-2:] # 2 most active

res = let_the_monkeys_do_simian_shenanigans(20, lambda n: n // 3)
print(math.prod([monkey["n_inspections"] for monkey in res]))

# segunda parte
res = let_the_monkeys_do_simian_shenanigans(10000, lambda n: n % LCM)
print(math.prod([monkey["n_inspections"] for monkey in res]))