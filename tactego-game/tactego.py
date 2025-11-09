import random

def read_pieces(file_name):
    red  = []
    blue = []
    # File is being open in read mode
    with open(file_name, 'r') as file:
        for line in file:
            # splits the line into seperate values
            pieces = line.split()
            for i in range(int(pieces[1])):
                red.append('r' + line[0])
                blue.append('b' + line[0])
                #shuffles each red and blue piece
        random.shuffle(red)
        random.shuffle(blue)


    return red, blue



def take_turn(board, players):
    red_player = players[0]
    blue_player = players[1]
    players_turn = red_player

    while True:
        if players_turn == "Red":
            print("Red player's turn")
            red_row = int(input("Select Piece to Move by Position (Enter row) "))
            red_column = int(input("Select Piece to Move by Position(Enter Column) >> "))
            red_piece = board[red_row][red_column]
            red_move_row = int(input("Enter a coordinate to move piece to (Enter row) "))
            red_move_column = int(input("Enter a coordinate to move piece to (Enter column) >> "))
            board[red_move_row][red_move_column] = red_piece
            board[red_row][red_column] = "0"
            draw_board(board)
        elif players_turn == blue_player:
            blue_row = int(input("Select Piece to Move by Position (Enter row) "))
            blue_column = int(input("Select Piece to Move by Position(Enter Column) >> "))
            blue_piece = board[blue_row][blue_column]
            blue_move_row = int(input("Enter a coordinate to move piece to (Enter row) "))
            blue_move_column = int(input("Enter a coordinate to move piece to (Enter column) >> "))
            board[blue_move_row][blue_move_column] = blue_piece
            board[blue_row][blue_column] = "0"
            draw_board(board)
        else:
            print("Invalid player. Please try again.")




def tactego(pieces_file, length, width):
    pieces = read_pieces(file_name)
    board = initialize_board(length, width)
    place_pieces(board, pieces)
    draw_board(board)
    players = ["Red", "Blue"]
    take_turn(board, players)



def initialize_board(length, width):
    return [[" " for _ in range(width)] for _ in range(length)]


def draw_board(board):
    # Print column numbers
    print("\t", end="")
    for col in range(len(board[0])):
        print(f"{col}\t", end="")
    print()

    # Print board with row numbers
    row_num = 0
    for row in board:
        print(f"{row_num}\t", end="")
        row_num += 1
        for cell in row:
            print(f"{cell}\t", end="", sep="")
        print()


def place_pieces(board, pieces):
    red_pieces = pieces[0]
    blue_pieces = pieces[1]

    for i in range(len(board) // 2):
        for j in range(len(board[0])):
            if red_pieces:
                value = random.choice(red_pieces)
                board[i][j] = value
                red_pieces.remove(value)

    for i in range(len(board) - 1, len(board) // 2 - 1, -1):
        for j in range(len(board[0])):
            if blue_pieces:
                value = random.choice(blue_pieces)
                board[i][j] = value
                blue_pieces.remove(value)

    def handle_assassin(board, row, col):
        piece = board[row][col]
        if piece[1] == 'A':
            opponent = 'B' if piece[0] == 'R' else 'R'
            print(f"Assassin eliminates {opponent}'s piece!")
            eliminate_opponent(board, row, col)

    def handle_mine(board, row, col):
        piece = board[row][col]
        if piece[1] == 'M':
            print("Mine exploded! Piece removed.")
            board[row][col] = '0'

    def eliminate_opponent(board, row, col):
        opponent = 'B' if board[row][col][0] == 'R' else 'R'
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c][0] == opponent:
                    print(f"{opponent}'s piece at ({r}, {c}) eliminated!")
                    board[r][c] = '0'

    def handle_combat(board, row, col):
        piece = board[row][col]
        opponent = find_opponent(board, row, col)

        if opponent:
            result = determine_combat_result(piece, opponent)
            print(f"Combat result: {result}")

            if result == 'Win':
                eliminate_opponent(board, *opponent)
            elif result == 'Lose':
                eliminate_opponent(board, row, col)

    def find_opponent(board, row, col):
        player = board[row][col][0]
        opponents = []

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c][0] != player and is_adjacent(row, col, r, c):
                    opponents.append((r, c))

        if opponents:
            return random.choice(opponents)
        else:
            return None


    def determine_combat_result(attacker, defender):
        if attacker[1] == 'A':
            return 'Win'
        elif defender[1] == 'A':
            return 'Lose'
        elif attacker[1] == 'S' and defender[1] == 'S':
            return 'Win'  # Sappers win by regular rules
        elif attacker[1] == 'M':
            return 'Win'
        elif defender[1] == 'M':
            return 'Lose'
        else:
            return 'Tie'





def update_board(board, start_pos, end_pos):
    row_start, col_start = start_pos
    row_end, col_end = end_pos
    board[row_end][col_end] = board[row_start][col_start]
    board[row_start][col_start] = ' '

def combat_outcome(result, player, board):
    if result > 0:
        print(f"Player {player} wins the combat!")
    elif result < 0:
        print(f"Player {player} loses the combat!")

def is_victory(board):
    red_flags = sum(cell[1:] == 'F' for row in board for cell in row if cell.startswith('R'))
    blue_flags = sum(cell[1:] == 'F' for row in board for cell in row if cell.startswith('B'))

    if red_flags == 0:
        return 'Blue'
    elif blue_flags == 0:
        return 'Red'
    else:
        return None





if __name__ == '__main__':
    random.seed(input('What is seed? '))
    file_name = input('What is the filename for the pieces? ')
    length = int(input('What is the length? '))
    width = int(input('What is the width? '))
    tactego(file_name, length, width)


