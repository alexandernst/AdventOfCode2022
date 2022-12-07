import re
from collections import defaultdict

current_dir = []
dirs = defaultdict(int)
for cmd in open("churro.txt", "r").read().splitlines():
  if folder := re.match(r"\$ cd (.+)", cmd):
    current_dir = current_dir[:-1] if folder.group(1) == ".." else [*current_dir, folder.group(1)]
  elif size := re.match(r"(\d+) .+", cmd):
    dirs[tuple(current_dir)] += int(size.group(1))
    # sum this size to every parent, because apparently elfic FS was created by PHP guys
    for i in range(1, len(current_dir)):
      dirs[tuple(current_dir[:-i])] += int(size.group(1))
print(sum(size for size in dirs.values() if size <= 100_000))

# segunda parte
required = abs(30_000_000 - (70_000_000 - sorted(dirs.values())[-1]))
print(next(size for size in sorted(dirs.values()) if size >= required))