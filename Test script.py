def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([2, 56, 2, 7, 4, 9, 4, 2,]))

game_size = 3
print("   " + "  ".join([str(i) for i in range(game_size)]))



