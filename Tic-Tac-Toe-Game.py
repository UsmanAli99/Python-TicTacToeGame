#  Tic Tac Toe Game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_still_going = True
winner = None
current_player = "A"


# -------------Game Start--------------
def play_game():
    global game_still_going
    global current_player
    while game_still_going:
        display_board()
        handle_input()
        check_game_end()
        flip_player()
    display_board()
    end_game()


# This Function will Display The Board....
def display_board():
    print(board[0], " | ", board[1], " | ", board[2], " | "
          , "       1  | 2  |  3")
    print(board[3], " | ", board[4], " | ", board[5], " | "
          , "       4  | 5  |  6")
    print(board[6], " | ", board[7], " | ", board[8], " | "
          , "       7  | 8  |  9")


# This function will handle the input in the desired position
def handle_input():
    global current_player
    print(f"{current_player}'s Turn .....")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            board[position] = current_player
            valid = True
        else:
            print("Sorry, You cannot use this place.....")
    print("\n\n ")


# This function will Flip turn to other player
def flip_player():
    global current_player
    if current_player == "A":
        current_player = "B"
    else:
        current_player = "A"


# This Function will Call check Win & Tie
def check_game_end():
    check_win()
    if not check_win():
        check_tie()


# This Function will check Win
def check_win():
    global game_still_going
    global winner
    global current_player
    if check_row_win() or check_column_win() or check_diagonal():
        game_still_going = False
        winner = current_player
        return True
    else:
        return False


# This function will check win from row wise
def check_row_win():
    if board[0] == board[1] == board[2] != "-":
        return True
    elif board[3] == board[4] == board[5] != "-":
        return True
    elif board[6] == board[7] == board[8] != "-":
        return True
    else:
        return False


# This function will check win from column wise
def check_column_win():
    if board[0] == board[3] == board[6] != "-":
        return True
    elif board[1] == board[4] == board[7] != "-":
        return True
    elif board[2] == board[5] == board[8] != "-":
        return True
    else:
        return False


# This function will check win from diagonal wise
def check_diagonal():
    if board[0] == board[4] == board[8] != "-":
        return True
    elif board[2] == board[4] == board[6] != "-":
        return True
    else:
        return False


# This function will check tie all after all positions are filled
def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False


# This Function will show the winner or show the tie message.......
def end_game():
    global winner
    if winner == "A" or winner == "B":
        print(f"{winner} won......")
    else:
        print("Game Tie......")


play_game()
