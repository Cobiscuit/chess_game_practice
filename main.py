import pygame
pygame.init()  # Must happen BEFORE importing constants

from board import Board
from constants import *

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
timer = TIMER  # This just points to the timer already made in constants.py

# Create the chessboard
board = Board()

# Start of the main game loop
running = True
while running:
    timer.tick(FPS)  # Control the frame rate
    screen.fill(BLACK)
    
    board.draw(screen)  # Draw the chessboard

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
