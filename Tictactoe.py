import itertools

def win(current_game):
    # Horizontal win:
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"player{row[0]} is the winner horizontally (—)!")

    # Diagonal win:
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"player{diags[0]} is the winner diagonally (/)!")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"player{diags[0]} is the winner diagonally (\\)!")

    # Vertical win:
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"player{check[0]} is the winner vertically (│)!")

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied, play another position. ")
            return game_map, False
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("Error: Try again. Input a integer that matches row/column.", e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False

play = True
players = [1, 2]
while play:
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play 0, 1 or 2 ?: "))
            row_choise = int(input("What row do you want to play 0, 1 or 2 ?: "))
            game, played = game_board(game, current_player, row_choise, column_choice)
            
#game = game_board(game, just_display=True)
#game = game_board(game, player=1, row=2, column=2)