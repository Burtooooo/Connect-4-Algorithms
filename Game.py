import sys
import random
import math
import numpy as np

P1_PIECE = 1
P2_PIECE = 2

ROW_COUNT = 6
COL_COUNT = 7

class Game:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = np.zeros((ROW_COUNT, COL_COUNT))
        return board

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(self, board, col):
        return board[ROW_COUNT - 1][col] == 0

    def get_valid_locations(self, board):
        valid_locations = []
        for col in range(COL_COUNT):
            if self.is_valid_location(board, col):
                valid_locations.append(col)
        return valid_locations

    def winning_move(self, board, piece):
        # Check horizontal locations for win
        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                    return True
        
        # Check vertical locations for win
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                    return True

        # Check positive-slope diagonals for win
        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                    return True

        # Check negative-slope diagonals for win
        for c in range(COL_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                    return True

    def is_terminal_node(self, board):
        # Check for end via win or via no moves left
        return self.winning_move(board, P1_PIECE) or self.winning_move(board, P2_PIECE) or len(self.get_valid_locations(board)) == 0

    def print_board(board):
        print(np.flip(board, 0))