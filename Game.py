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

    def drop_piece(self, col, piece):
        for i in range(ROW_COUNT):
            if self.board[i][col] == 0:
                self.board[i][col] = piece
                return

    def is_valid_location(self, col):
        return self.board[ROW_COUNT - 1][col] == 0

    def get_valid_locations(self):
        valid_locations = []
        for col in range(COL_COUNT):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def winning_move(self, piece):
        # Check horizontal locations for win
        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and self.board[r][c + 3] == piece:
                    return True
        
        # Check vertical locations for win
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and self.board[r + 3][c] == piece:
                    return True

        # Check positive-slope diagonals for win
        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == piece and self.board[r + 3][c + 3] == piece:
                    return True

        # Check negative-slope diagonals for win
        for c in range(COL_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] == piece and self.board[r - 3][c + 3] == piece:
                    return True

    def is_terminal_node(self):
        # Check for end via win or via no moves left
        return self.winning_move(P1_PIECE) or self.winning_move(P2_PIECE) or len(self.get_valid_locations()) == 0

    def game_score(self):
        #For terminal game return score 
        if (self.winning_move(P1_PIECE)):
            return 1
        if (self.winning_move(P2_PIECE)):
            return -1
        if (len(self.get_valid_locations()) == 0):
            return 0

        raise Exception("Only call game_score on terminal board")

    def print_board(self):
        print(np.flip(self.board, 0))
        return 0

    def h_3inrow(self, piece):

        num3inrow = 0
        
        if piece == 1:
            piece2 = 2
        else:
            piece2 = 1
        # Check horizontal locations for win
        for c in range(COL_COUNT - 2):
            for r in range(ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece:
                    num3inrow += 1

        # Check vertical locations for win
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 2):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece:
                    num3inrow += 1

        # Check positive-slope diagonals for win
        for c in range(COL_COUNT - 2):
            for r in range(ROW_COUNT - 2):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == piece:
                    num3inrow += 1

        # Check negative-slope diagonals for win
        for c in range(COL_COUNT - 2):
            for r in range(2, ROW_COUNT):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] == piece:
                    num3inrow += 1

        
        for c in range(COL_COUNT - 2):
            for r in range(ROW_COUNT):
                if self.board[r][c] == piece2 and self.board[r][c + 1] == piece2 and self.board[r][c + 2] == piece2:
                    num3inrow -= 1

        # Check vertical locations for win
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 2):
                if self.board[r][c] == piece2 and self.board[r + 1][c] == piece2 and self.board[r + 2][c] == piece2:
                    num3inrow -= 1

        # Check positive-slope diagonals for win
        for c in range(COL_COUNT - 2):
            for r in range(ROW_COUNT - 2):
                if self.board[r][c] == piece2 and self.board[r + 1][c + 1] == piece2 and self.board[r + 2][c + 2] == piece2:
                    num3inrow -= 1

        # Check negative-slope diagonals for win
        for c in range(COL_COUNT - 2):
            for r in range(2, ROW_COUNT):
                if self.board[r][c] == piece2 and self.board[r - 1][c + 1] == piece2 and self.board[r - 2][c + 2] == piece2:
                    num3inrow -= 1

        return num3inrow