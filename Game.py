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

    def get_row_num(self, col):
        for i in range(ROW_COUNT):
            if self.board[i][col] == 0:
                return i

    def successor(self, col, piece):
        successor_board = self.board.copy()
        for i in range(ROW_COUNT):
            if successor_board[i][col] == 0:
                successor_board[i][col] = piece
                break
        
        return successor_board

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
        print()
        return 0

    def h_rand(self):

        #This is reutrn a constantbecause built into the decision 
        #Algs is to randomly choose equal values
        return 0

    def h_middle(self):
        #This is less of a heurisitc and more of a policy
        #If there isnt an obvious move at given depth,
        #Prioritize playing in the center column

        #This is unpopulated because the actual logic is handled in alpha beta
        return 0

    def h_touching(self):
        #This herusitic counts the difference in the number of total way
        #Player 1s tiles touch minus total ways player 2s tiles touch

        numtouching = 0
        piece = P1_PIECE
        piece2 = P2_PIECE
        # Check horizontal locations for win
        for c in range(COL_COUNT - 1):
            for r in range(ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece:
                    numtouching += 1
                if self.board[r][c] == piece2 and self.board[r][c + 1] == piece2:
                    numtouching -= 1

        # Check vertical locations for win
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 1):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece:
                    numtouching += 1
                if self.board[r][c] == piece2 and self.board[r + 1][c] == piece2:
                    numtouching -= 1

        # Check positive-slope diagonals for win
        for c in range(COL_COUNT - 1):
            for r in range(ROW_COUNT - 1):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece:
                    numtouching += 1
                if self.board[r][c] == piece2 and self.board[r + 1][c + 1] == piece2:
                    numtouching -= 1

        # Check negative-slope diagonals for win
        for c in range(COL_COUNT - 1):
            for r in range(1, ROW_COUNT):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece:
                    numtouching += 1
                if self.board[r][c] == piece2 and self.board[r - 1][c + 1] == piece2:
                    numtouching -= 1

        return numtouching

    def h_3inrow(self):
        #this heuristic counts the difference in number
        #of 3 in a rows of player 1 and player 2

        num3inrow = 0
        
        piece = P1_PIECE
        piece2 = P2_PIECE
        # Check horizontal locations for win
        for c in range(COL_COUNT - 2):
            for r in range(ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece:
                    num3inrow += 1
                if self.board[r][c] == piece2 and self.board[r][c + 1] == piece2 and self.board[r][c + 2] == piece2:
                    num3inrow -= 1

        # Check vertical locations for win
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 2):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece:
                    num3inrow += 1
                if self.board[r][c] == piece2 and self.board[r + 1][c] == piece2 and self.board[r + 2][c] == piece2:
                    num3inrow -= 1

        # Check positive-slope diagonals for win
        for c in range(COL_COUNT - 2):
            for r in range(ROW_COUNT - 2):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == piece:
                    num3inrow += 1
                if self.board[r][c] == piece2 and self.board[r + 1][c + 1] == piece2 and self.board[r + 2][c + 2] == piece2:
                    num3inrow -= 1

        # Check negative-slope diagonals for win
        for c in range(COL_COUNT - 2):
            for r in range(2, ROW_COUNT):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] == piece:
                    num3inrow += 1
                if self.board[r][c] == piece2 and self.board[r - 1][c + 1] == piece2 and self.board[r - 2][c + 2] == piece2:
                    num3inrow -= 1

        return num3inrow

    def h_2x1(self):
        #this heuristic counts the number of 3 in a row and 2-gap-1

        num = self.h_3inrow()
        num = 0

        piece = P1_PIECE
        piece2 = P2_PIECE

        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c + 1] == 0 and self.board[r][c + 2] == piece and self.board[r][c + 3] == piece:
                    num+=1
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == 0 and self.board[r][c + 3] == piece:
                    num+=1

                if self.board[r][c] == piece2 and self.board[r][c + 1] == 0 and self.board[r][c + 2] == piece2 and self.board[r][c + 3] == piece2:
                    num-=1
                if self.board[r][c] == piece2 and self.board[r][c + 1] == piece2 and self.board[r][c + 2] == 0 and self.board[r][c + 3] == piece2:
                    num-=1

        # Check vertical locations for win
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == piece and self.board[r + 1][c] == 0 and self.board[r + 2][c] == piece and self.board[r + 3][c] == piece:
                    num+=1
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == 0 and self.board[r + 3][c] == piece:
                    num+=1

                if self.board[r][c] == piece2 and self.board[r + 1][c] == 0 and self.board[r + 2][c] == piece2 and self.board[r + 3][c] == piece2:
                    num-=1
                if self.board[r][c] == piece2 and self.board[r + 1][c] == piece2 and self.board[r + 2][c] == 0 and self.board[r + 3][c] == piece2:
                    num-=1

        # Check positive-slope diagonals for win
        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == 0 and self.board[r + 3][c + 3] == piece:
                    num+=1
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == 0 and self.board[r + 2][c + 2] == piece and self.board[r + 3][c + 3] == piece:
                    num+=1

                if self.board[r][c] == piece2 and self.board[r + 1][c + 1] == piece2 and self.board[r + 2][c + 2] == 0 and self.board[r + 3][c + 3] == piece2:
                    num-=1
                if self.board[r][c] == piece2 and self.board[r + 1][c + 1] == 0 and self.board[r + 2][c + 2] == piece2 and self.board[r + 3][c + 3] == piece2:
                    num-=1

        # Check negative-slope diagonals for win
        for c in range(COL_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] == 0 and self.board[r - 3][c + 3] == piece:
                    num+=1
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == 0 and self.board[r - 2][c + 2] == piece and self.board[r - 3][c + 3] == piece:
                    num+=1

                if self.board[r][c] == piece2 and self.board[r - 1][c + 1] == piece2 and self.board[r - 2][c + 2] == 0 and self.board[r - 3][c + 3] == piece2:
                    num-=1
                if self.board[r][c] == piece2 and self.board[r - 1][c + 1] == 0 and self.board[r - 2][c + 2] == piece2 and self.board[r - 3][c + 3] == piece2:
                    num-=1
        return num