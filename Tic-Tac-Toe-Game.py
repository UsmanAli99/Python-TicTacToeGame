#  Tic Tac Toe Game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_still_going = True
winner = None
current_player = "A"


def play_game():
    global game_still_going
    global current_player
    while game_still_going:
        display_board()
        handle_input(current_player)
        flip_player(current_player)


def display_board():
    print(board[0], " | ", board[1], " | ", board[2], " | "
          , "       1  | 2  |  3")
    print(board[3], " | ", board[4], " | ", board[5], " | "
          , "       4  | 5  |  6")
    print(board[6], " | ", board[7], " | ", board[8], " | "
          , "       7  | 8  |  9")


def handle_input(current):
    print(f"{current}'s Turn .....")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            board[position] = current
            valid = True
        else:
            print("Sorry, You cannot use this place.....")
    print("\n\n ")


def flip_player(flip):
    global current_player
    if flip == "A":
        current_player = "B"
    else:
        current_player = "A"


play_game()
