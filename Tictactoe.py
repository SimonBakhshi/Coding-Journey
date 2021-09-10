import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        return False

    # Horizontal win:
    for row in game:
        print(row)
        if all_same(row):
            print(f"player{row[0]} is the winner horizontally (—)!")
            return True

    # Diagonal win:
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"player{diags[0]} is the winner diagonally (/)!")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"player{diags[0]} is the winner diagonally (\\)!")
        return True

    # Vertical win:
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"player{check[0]} is the winner vertically (│)!")
            return True
    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied, play another position. ")
            return game_map, False
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))
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
    
    game_size = int(input("What size game of Tic tac toe do you want? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
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
        
        if win(game):
            game_won = True
            again = input("The game is over, do you want to play again? (y/n) ")
            if again.lower() == "y":
                print("The game is restarting... ")
            elif again.lower() == "n":
                print("see yaaaaaa! ")
                play = False
            else:
                print("That is not a valid answer, hope to see you again soon ")
                play = False