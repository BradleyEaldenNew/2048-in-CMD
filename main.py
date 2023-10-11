import os
import random

def check_win(board):
    for row in board:
        if 64 in row:
            return True
    return False

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_board(board):
    clear_screen()
    size = len(board)
    color_map = {
        0: '\033[30;1m',
        2: '\033[34;1m',
        4: '\033[32;1m',
        8: '\033[31;1m',
        16: '\033[35;1m',
        32: '\033[36;1m',
        64: '\033[32;1m',
    }
    end_color = '\033[0m'

    for i in range(size):
        for j in range(size):
            cell_value = board[i][j]
            formatted_value = f"{cell_value:02}" if cell_value > 0 else "00"  # Updated this line
            color = color_map.get(cell_value, '\033[37;1m')  # Default to white

            print(f"{color}{formatted_value}{end_color}", end=" ")
        print()

def generate_new_tile(board):
    size = len(board)
    empty_cells = [(i, j) for i in range(size) for j in range(size) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2

def move_board_up(board):
    size = len(board)
    for col in range(size):
        non_zero_elements = []

        for row in range(size):
            if board[row][col] != 0:
                non_zero_elements.append(board[row][col])

        for i in range(len(non_zero_elements) - 1):
            if non_zero_elements[i] == non_zero_elements[i + 1]:
                non_zero_elements[i] *= 2
                non_zero_elements[i + 1] = 0

        non_zero_elements = [elem for elem in non_zero_elements if elem != 0]

        while len(non_zero_elements) < size:
            non_zero_elements.append(0)

        for row in range(size):
            board[row][col] = non_zero_elements[row]

def move_board_left(board):
    size = len(board)
    
    for row in range(size):
        non_zero_elements = []

        for col in range(size):
            if board[row][col] != 0:
                non_zero_elements.append(board[row][col])

        for i in range(len(non_zero_elements) - 1):
            if non_zero_elements[i] == non_zero_elements[i + 1]:
                non_zero_elements[i] *= 2
                non_zero_elements[i + 1] = 0

        non_zero_elements = [elem for elem in non_zero_elements if elem != 0]

        while len(non_zero_elements) < size:
            non_zero_elements.append(0)

        for col in range(size):
            board[row][col] = non_zero_elements[col]

def move_board_right(board):
    size = len(board)

    for row in range(size):
        non_zero_elements = []

        for col in range(size - 1, -1, -1):
            if board[row][col] != 0:
                non_zero_elements.append(board[row][col])

        for i in range(len(non_zero_elements) - 1):
            if non_zero_elements[i] == non_zero_elements[i + 1]:
                non_zero_elements[i] *= 2
                non_zero_elements[i + 1] = 0

        non_zero_elements = [elem for elem in non_zero_elements if elem != 0]

        while len(non_zero_elements) < size:
            non_zero_elements.insert(0, 0)

        for col in range(size):
            board[row][col] = non_zero_elements[col]

def move_board_down(board):
    size = len(board)

    for col in range(size):
        non_zero_elements = []

        for row in range(size):
            if board[row][col] != 0:
                non_zero_elements.append(board[row][col])

        for i in range(len(non_zero_elements) - 1, 0, -1):
            if non_zero_elements[i] == non_zero_elements[i - 1]:
                non_zero_elements[i] *= 2
                non_zero_elements[i - 1] = 0

        non_zero_elements = [elem for elem in non_zero_elements if elem != 0]

        while len(non_zero_elements) < size:
            non_zero_elements.insert(0, 0)

        for row in range(size):
            board[row][col] = non_zero_elements[row]

board = [
    [2, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 0, 0]
]

while True:
    print_board(board)

    if check_win(board):
        print("YOU WON!")
        break

    x = input("Press WASD: ")

    if x == "w":
        move_board_up(board)
        generate_new_tile(board)
    elif x == "a":
        move_board_left(board)
        generate_new_tile(board)
    elif x == "d":
        move_board_right(board)
        generate_new_tile(board)
    elif x == "s":
        move_board_down(board)
        generate_new_tile(board)
