import pygame

class Board():
    """Board game"""
    def __init__(self, surface, file, square_size, number_of_squares, size):
        self.surface = surface
        self.file = file
        self.structure = []
        self.square_size = square_size
        self.number_of_squares = number_of_squares
        self.size = size

    def generate(self):
        """Generate the board in self.structure"""
        self.structure = []
        with open(self.file, "r") as file:
            for line in file:
                row = [square for square in line if square != '\n']
                self.structure.append(row)
    
    def draw_lines(self, color=(0, 0, 0)):
        for i in range(self.number_of_squares):
            pygame.draw.line(self.surface, color, (self.square_size // 2 + self.square_size * i, self.square_size // 2), (self.square_size // 2 + self.square_size * i, self.size - self.square_size // 2))
            pygame.draw.line(self.surface, color, (self.square_size // 2, self.square_size // 2 + self.square_size * i), (self.size - self.square_size // 2, self.square_size // 2 + self.square_size * i))

    def show(self, color1=(0, 0, 0), color2=(255, 255, 255)):
        for i in range(len(self.structure)):
            for j in range(len(self.structure[i])):
                if self.structure[i][j] == 'b':
                    pygame.draw.circle(self.surface, color1, (self.square_size // 2 + j * self.square_size, self.square_size // 2 + i * self.square_size), self.square_size // 2)
                elif self.structure[i][j] == 'w':
                    pygame.draw.circle(self.surface, color2, (self.square_size // 2 + j * self.square_size, self.square_size // 2 + i * self.square_size), self.square_size // 2)

    def isValide(self, x, y):
        x = int(round_number(x) // 40)
        y = int(round_number(y) // 40)
        return self.structure[y][x] == 'a'

    def draw_token(self, x, y, player):
        x = int(round_number(x) // 40)
        y = int(round_number(y) // 40)
        self.structure[y][x] = player
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.structure[y + i][x + j] == 'e': 
                    self.structure[y + i][x + j] = 'a'

    def isFinished(self,player):
        s = self.structure
        for i in range(self.number_of_squares):
            for j in range(self.number_of_squares):
                if s[i][j] == player:
                    # top
                    if i > 3:
                        if s[i-1][j] == s[i-2][j] == s[i-3][j] == s[i-4][j]: return True
                    # top left
                    if i > 3 and j >= i:
                        if s[i-1][j-1] == s[i-2][j-2] == s[i-3][j-3] == s[i-4][j-4]: return True
                    # left
                    if j > 3:
                        if s[i][j-1] == s[i][j-2] == s[i][j-3] == s[i][j-4]: return True
                    # bottom left
                    if i < self.number_of_squares - 3 and j > 3:
                        if s[i+1][j-1] == s[i+2][j-2] == s[i+3][j-3] == s[i+4][j-4]: return True
                    # bottom
                    if i < self.number_of_squares -3:
                        if s[i+1][j] == s[i+2][j] == s[i+3][j] == s[i+4][j]: return True
                    #bottom right
                    if i < self.number_of_squares - 3 and j <= i:
                        if s[i+1][j+1] == s[i+2][j+2] == s[i+3][j+3] == s[i+4][j+4]: return True
                    # right
                    if j < self.number_of_squares - 3:
                        if s[i][j+1] == s[i][j+2] == s[i][+3] == s[i][+4]: return True
                    # top right
                    if i > 3 and j < self.number_of_squares - 3:
                        if s[i-1][j+1] == s[i-2][j+2] == s[i-3][j+3] == s[i-4][j+4]: return True
        return False

def round_number(n):
    if n >= 0 and n < 40: return 20
    elif n >= 40 and n < 80: return 60
    elif n >= 80 and n < 120: return 100
    elif n >= 120 and n < 160: return 140
    elif n >= 160 and n < 200: return 180
    elif n >= 200 and n < 240: return 220
    elif n >= 240 and n < 280: return 260
    elif n >= 280 and n < 320: return 300
    elif n >= 320 and n < 360: return 340
    elif n >= 360 and n < 400: return 380
    elif n >= 400 and n < 440: return 420
    elif n >= 440 and n < 480: return 460
    elif n >= 480 and n < 520: return 500
    elif n >= 520 and n < 560: return 540
    elif n >= 560 and n < 600: return 580
    elif n >= 600 and n < 640: return 620
    elif n >= 640 and n < 680: return 640
    elif n >= 680 and n < 720: return 700
    elif n >= 720 and n <= 760: return 740