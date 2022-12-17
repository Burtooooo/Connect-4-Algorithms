import time
import math
import random
from Game import Game

P1_PIECE = 1
P2_PIECE = 2

ROW_COUNT = 6
COL_COUNT = 7

class MCTS:
    def __init__(self, game):
        self.game = game
        self.current_path = []
        self.state_dict = {}
        self.action_dict = {}
        self.children_dict = {}

def mcts_run(allowed_time):
    mcts_manager = MCTS()
    def mcts(start_pos, allowed_time, mcts_manager):
        if start_pos not in mcts_manager.state_dict:
            mcts_manager.expand(start_pos)

        time_end = time.time() + allowed_time
        while time.time() < time_end:
            mcts_manager.run(start_pos)

        return mcts_manager.find_best_action(start_pos)

    def fxn(start_pos):
        best_move = mcts(start_pos, allowed_time, mcts_manager)
        return best_move

    return fxn