from tkinter import Frame, Label, LabelFrame, Button, Canvas

from constants import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.menu()
        
    def menu(self):
        self.master.title('Gomoku')
        Label(self, text='GOMOKU').pack(side='top', pady=20)
        self.frame = LabelFrame(self, text='Rules')
        Label(self.frame, text="The player who has drawn black pieces always plays first\nby placing his first piece on the central intersection of the checkerboard.\nWhite must then place his pawn on one of the 8 intersections adjacent to the Black pawn.\nBlack does the same, and so on, the object of the game being to take the opponent by speed and\nto be the first to line up 5 checkers of his color, in the three possible directions: vertical, horizontal or diagonal.").pack()
        Button(self.frame, text='PLAY', command=self.play).pack(pady=40, ipadx=20, ipady=10)
        self.frame.pack(side='top', padx=20, pady=10)

    def play(self):
        self.board = Board(self)

class Board(Application):
    """Create a checkered board of size nb_squares ** 2"""
    def __init__(self, app):
        self.player = 1
        self.finished = False
        self.first_token = True
        self.nb_token_placed = 0
        self.board = Canvas(app, width=board_size, height=board_size, background="#fb9d4e")
        for i in range(square_size // 2, board_size - square_size // 2 + 1, square_size):
            self.board.create_line(square_size / 2, i, board_size - square_size / 2, i)
            self.board.create_line(i, square_size / 2, i, board_size - square_size / 2)
        self.board.create_oval(nb_squares // 2 * 40 + 2, nb_squares // 2 * 40 + 2, nb_squares // 2 * 40 + 38, nb_squares // 2 * 40 + 38, outline='black', fill='black')
        board_arr[nb_squares // 2][nb_squares // 2] = 'w'
        self.board.pack(expand=True)
        self.board.bind('<Button-1>', self.click)

    def click(self, event):
        """Draw a token on the nearest cross of the click"""
        x, y = round(float(event.x - 20) / 40) * 40 + 20, round(float(event.y - 20) / 40) * 40 + 20
        if board_arr[y // 40][x // 40] == 'e' and (board_arr[y // 40 - 1][x // 40] != 'e' or board_arr[y // 40 - 1][x // 40 - 1] != 'e' or board_arr[y // 40][x // 40 - 1] != 'e' or board_arr[y // 40 + 1][x // 40 - 1] != 'e' or board_arr[y // 40 + 1][x // 40] != 'e' or board_arr[y // 40 + 1][x // 40 + 1] != 'e' or board_arr[y // 40][x // 40 + 1] != 'e' or board_arr[y // 40 - 1][x // 40 + 1] != 'e'):
            self.nb_token_placed += 1
            if self.player == 0:
                board_arr[y // 40][x // 40] = 'd'
                self.board.create_oval(x - 18, y - 18, x + 18, y + 18, outline='black', fill='black')
                self.player = 1
            else:
                board_arr[y // 40][x // 40] = 'w'
                self.board.create_oval(x - 18, y - 18, x + 18, y + 18, outline='white', fill='white')
                self.player = 0
            self.board.pack()
            self.isFinished(x, y)
            if self.finished or self.nb_token_placed == nb_tokens_max:
                self.board.bind('<Button-1>', self.r)
                print(self.nb_token_placed)
                print('finished')
        return

    def isFinished(self, j, i):
        """Check if five token are aligned. j is x and i is y"""
        j //= 40
        i //= 40
        a = board_arr[i][j]
        if (i > 3 and board_arr[i - 1][j] == a and board_arr[i - 2][j] == a and board_arr[i - 3][j] == a and board_arr[i - 4][j] == a) \
        or (j > 3 and board_arr[i][j - 1] == a and board_arr[i][j - 2] == a and board_arr[i][j - 3] == a and board_arr[i][j - 4] == a) \
        or (i < nb_squares - 4 and board_arr[i + 1][j] == a and board_arr[i + 2][j] == a and board_arr[i + 3][j] == a and board_arr[i + 4][j] == a) \
        or (j < nb_squares - 4 and board_arr[i][j + 1] == a and board_arr[i][j + 2] == a and board_arr[i][j + 3] == a and board_arr[i][j + 4] == a): # top left bottom right
            self.finished = True
            print(a)
            print(i, j)
            return

    def r(self, *args):
        return 0