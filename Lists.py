tictactoe = [ ['X', 'O', 'X'],
              [ 'O', ' ', 'X'],
              ['X','O','O']]

for row in tictactoe:
    for column in row:
        print(column + " ", end='')
    print()