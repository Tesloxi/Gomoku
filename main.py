#!/usr/bin/python3
# -*- coding: utf-8 -*

"""Gomoku game using pygame"""

import pygame
import os
from classes import *

pygame.init()

# CONSTANTS
SQUARE_SIZE = 40
NUMBER_OF_SQUARES = 19
SIZE = SQUARE_SIZE * NUMBER_OF_SQUARES
NUMBER_OF_TOKEN_MAX = 120

# COLORS
BEIGE = (245, 245, 220)
BLACK = (0, 0, 0)

# FONTS
MENU_TITLE_FONT = pygame.font.SysFont('comicsans', 100)
MENU_BUTTONS_FONT = pygame.font.SysFont('comicsans', 50)

# setup menu
os.environ['SDL_VIDEO_WINDOW_POS'] = "400,100"
win = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Gomoku")


menu = pygame.Surface((SIZE, SIZE))
menu.fill(BEIGE)

def show_menu():
    win.blit(menu, (0, 0))
    
    text = MENU_TITLE_FONT.render('GOMOKU', 1, BLACK)
    win.blit(text, (SIZE // 2 - text.get_width() // 2, 100))

    button_pvb = pygame.Rect(SIZE // 6, 400, SIZE // 4, 100)
    pygame.draw.rect(win, BLACK, button_pvb, 1)
    text = MENU_BUTTONS_FONT.render('PVB', 1, BLACK)
    win.blit(text, (button_pvb.left + button_pvb.width // 2 - text.get_width() // 2, button_pvb.top + button_pvb.height // 2 - text.get_height() // 2))

    global button_pvp
    button_pvp = pygame.Rect(SIZE // 6 * 2 + SIZE // 4, 400, SIZE // 4, 100)
    pygame.draw.rect(win, BLACK, button_pvp, 1)
    text = MENU_BUTTONS_FONT.render('PVP', 1, BLACK)
    win.blit(text, (button_pvp.left + button_pvp.width // 2 - text.get_width() // 2, button_pvp.top + button_pvp.height // 2 - text.get_height() // 2))

show_menu()

game = pygame.Surface((SIZE, SIZE))
game.fill(BEIGE)
board = Board(win, './map.txt', SQUARE_SIZE, NUMBER_OF_SQUARES, SIZE)
board.generate()

# setup game loop
FPS = 30
clock = pygame.time.Clock()
run = True
run_menu = True
run_game = True

mode = ''
turn = 'w'
number_of_token_placed = 1

while run:
    clock.tick(FPS)

    for event in pygame.event.get():     
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): run = False

    while run_menu:
        for event in pygame.event.get():     
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                run_menu = False
                run = False
            # click on pvp
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_pvp.collidepoint(event.pos):
                    mode = 'pvp'
                    win.blit(game, (0, 0))
                    board.draw_lines()
                    run_menu = False
                    if not run_game: run_game = True
                    board.generate()
                    
        pygame.display.update()
        

    while run_game:
        for event in pygame.event.get():     
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                run_game = False
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if number_of_token_placed < NUMBER_OF_TOKEN_MAX:
                    if mode == 'pvp':
                        x, y = event.pos
                        if board.isValide(x, y):
                            board.draw_token(x, y, turn)
                            number_of_token_placed += 1
                            if number_of_token_placed >= 9:
                                run_game = not board.isFinished(turn)
                                run_menu = not run_game
                            if turn == 'w': turn = 'b'
                            else: turn = 'w'
        board.show()
        pygame.display.update()
    
    show_menu()

pygame.quit()