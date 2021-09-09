def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([2, 56, 2, 7, 4, 9, 4, 2,]))

import itertools
player_choice = itertools.cycle([1, 2])

for i in range(10):
    print(next(player_choice))