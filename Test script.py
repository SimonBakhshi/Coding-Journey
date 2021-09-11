def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([2, 56, 2, 7, 4, 9, 4, 2,]))


'''game = []
for i in range(game_size):
  row = []
  for i in range(game_size):
    row.append(0)
  game.append(row)
print(game)'''

'''game_size = int(input("What size game of Tic tac toe do you want? "))
game = [[0 for i in range(game_size)] for i in range(game_size)]
print(game)'''


x = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
x[1][2] = 9
print(x)