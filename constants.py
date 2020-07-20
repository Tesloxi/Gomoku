"""Here are the constants of the gomoku project"""

square_size = 40
nb_squares = 19
board_size = square_size * nb_squares
nb_tokens_max = 120
board_arr = []
for _ in range(nb_squares):
    board_arr.append(['e'] * nb_squares)