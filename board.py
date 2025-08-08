import pygame
from constants import *

class Board:
    def __init__(self):
        self.rows = 8
        self.columns = 8
        self.square_size = WINDOW_HEIGHT // self.rows  # use height to keep it square
        self.board = self.create_board()

    def create_board(self):
        board = {}
        files = "ABCDEFGH"
        ranks = "87654321"

        for rank in ranks:
            for file in files:
                square = f"{file}{rank}"
                board[square] = None
        return board

    def get_square_rect(self, file, rank):
        col = "ABCDEFGH".index(file)
        row = "87654321".index(rank)
        x = col * self.square_size
        y = row * self.square_size
        return pygame.Rect(x, y, self.square_size, self.square_size)

    def draw(self, screen):
        for square in self.board:
            file = square[0]
            rank = square[1]
            rect = self.get_square_rect(file, rank)

            col = "ABCDEFGH".index(file)
            row = "87654321".index(rank)

            # Alternate light/dark square colors
            if (row + col) % 2 == 0:
                color = LIGHT_BROWN
            else:
                color = DARK_BROWN

            pygame.draw.rect(screen, color, rect)