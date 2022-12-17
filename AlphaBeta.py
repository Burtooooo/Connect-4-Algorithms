from Game import Game
from random import randint


P1_PIECE = 1
P2_PIECE = 2

ROW_COUNT = 6
COL_COUNT = 7

MIN = -1000
MAX = 1000


class AB:
    def __init__(self, depth, heur):
        self.game = None
        self.depth = depth
        self.heur = heur

    def ab_search(self, depth, player, alpha, beta):
        
        if (self.game.is_terminal_node()):
            return (500 * self.game.game_score()) + depth
        
        if depth == 0:
            if self.heur == "3inrow":
                return self.game.h_3inrow(1)
            elif self.heur == "rand":
                #NOT TRULY RANDOM, WILL FIND WIN OR AVOID LOSS IN DEPTH
                return self.game.h_rand()
            raise Exception("Non valid heur")



        if player == 1:
            cur_best = MIN

            valid_locations = self.game.get_valid_locations()

            hold_board = self.game.board.copy()
            for i in range(len(valid_locations)):
                self.game.drop_piece(valid_locations[i], 1)
                val = self.ab_search(depth - 1, 2, alpha, beta)
                cur_best = max(cur_best, val)
                alpha = max(alpha, cur_best)
                self.game.board = hold_board.copy()
                if beta <= alpha:
                    break

            return cur_best
        
        else:
            cur_best = MAX

            valid_locations = self.game.get_valid_locations()

            hold_board = self.game.board.copy()
            for i in range(len(valid_locations)):
                self.game.drop_piece(valid_locations[i], 2)
                val = self.ab_search(depth - 1, 1, alpha, beta)
                cur_best = min(cur_best, val)
                beta = min(beta, cur_best)
                self.game.board = hold_board.copy()
                if beta <= alpha:
                    break

            return cur_best

    def find_move(self, player):
        if player == 1:
            cur_best = MIN
            valid_locations = self.game.get_valid_locations()
            best_moves = []
            hold_board = self.game.board.copy()
            for i in range(len(valid_locations)):
                self.game.drop_piece(valid_locations[i], 1)
                val = self.ab_search(self.depth - 1, 2, MIN, MAX)
                if(val>cur_best):
                    best_moves.clear()
                    best_moves.append(valid_locations[i])
                    cur_best = val
                elif(val == cur_best):
                    best_moves.append(valid_locations[i])
                self.game.board = hold_board.copy()
        
            #for i in range(len(best_moves)):
            #    self.game.drop_piece(best_moves[i], 1)
            self.game.drop_piece(best_moves[randint(0, len(best_moves) - 1)], 1)

        else:
            cur_best = MAX
            valid_locations = self.game.get_valid_locations()
            best_moves = []
            hold_board = self.game.board.copy()
            for i in range(len(valid_locations)):
                self.game.drop_piece(valid_locations[i], 2)
                val = self.ab_search(self.depth - 1, 1, MIN, MAX)
                if(val<cur_best):
                    best_moves.clear()
                    best_moves.append(valid_locations[i])
                    cur_best = val
                elif(val == cur_best):
                    best_moves.append(valid_locations[i])
                self.game.board = hold_board.copy()
        
            # for i in range(len(best_moves)):
            #     self.game.drop_piece(best_moves[i], 2)
            self.game.drop_piece(best_moves[randint(0, len(best_moves) - 1)], 2)



# myGame = Game()

# #Not truly random, will find win or avoid loss at depth 1
# myAB = AB(5, "3inrow")
# myAB.game = myGame

#myGame.print_board()
# myGame.drop_piece(2, 1)
# myGame.drop_piece(5, 2)
# myGame.drop_piece(4, 1)
# myGame.drop_piece(5, 2)
# myGame.drop_piece(3, 1)
# myGame.drop_piece(3, 2)
# myGame.drop_piece(4, 1)
# myGame.drop_piece(2, 2)
# myGame.drop_piece(2, 1)
# myGame.drop_piece(2, 2)
# myGame.drop_piece(6, 1)
# myGame.drop_piece(5, 2)
# myGame.drop_piece(3, 1)
# myGame.drop_piece(3, 2)
# myGame.drop_piece(4, 1)
# myGame.drop_piece(4, 2)

# myGame.drop_piece(4, 1)
# myGame.drop_piece(1, 1)
# myGame.drop_piece(4, 1)
# myAB.find_move(1)
# myGame.print_board()