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

    def mcts_search(self, time, player):
        pass

    def run(self, root_state, root_player):
        res_state = self.traverse(root_state)
        self.expand(res_state)
        self.simulate(res_state)

    def traverse(self, root_state):
        self.current_path = []
        current_state = root_state
        while True:
            self.current_path.append(current_state)
            if Game.is_terminal_node(current_state):
                return current_state
            else:
                available_next_states = self.state_dict[current_state][3]
                for next_state in available_next_states:
                    if next_state not in self.state_dict:
                        self.current_path.append(next_state)
                        return next_state
                # Run UCB-2
                current_state = self.ucb_evaluate(current_state)

    def expand(self, state):
        if state not in self.state_dict:
            self.state_dict[state] = [0, 0, [], []]
            self.get_child_actions_and_states(state)

    def simulate(self, state):
        while not Game.is_terminal_node(state):
            # Get a list of available columns (aka moves/actions) to drop a piece into
            available_actions = Game.get_valid_locations()
            selected_action = random.choice(available_actions)
            # Need to change piece depending on who's turn it is
            piece = P1_PIECE if Game.get_player() == 1 else P2_PIECE
            Game.drop_piece(selected_action, piece)
            state = self.game.board
        payoff = Game.game_score()
        self.update(payoff)

    def update(self, payoff):
        for state in self.current_path:
            entry = self.state_dict[state]
            entry[0] += payoff
            entry[1] += 1

    def get_child_actions_and_states(self, state):
        available_actions = Game.get_valid_locations()
        for action in available_actions:
            self.state_dict[state][2].append(action)
            # Need to change piece depending on who's turn it is
            self.state_dict[state][3].append(Game.successor(action, P1_PIECE))

    def ucb_evaluate(self, parent_state):
        best_ucb_score = 0
        pass

    # Given a state and a player to move, returns the best move for that player
    def find_move(self, root_state, root_player):
        best_score = 0
        best_action = None

        if root_player == 1:
            best_score = float("-inf")
        else:
            best_score = float("inf")

        for index, next_state in enumerate(self.state_dict[root_state][3]):
            next_state_score = self.state_dict[next_state][0] / self.state_dict[next_state][1]
            if root_player == 1:
                if next_state_score > best_score:
                    best_score = next_state_score
                    best_action = self.state_dict[root_state][2][index]
            else:
                if next_state_score < best_score:
                    best_score = next_state_score
                    best_action = self.state_dict[root_state][2][index]

        return best_action


def mcts_policy(Game, allowed_time):
    mcts_manager = MCTS()
    def mcts(root_state, allowed_time, mcts_manager):
        if root_state not in mcts_manager.state_dict:
            mcts_manager.expand(root_state)

        time_end = time.time() + allowed_time
        while time.time() < time_end:
            root_player = 1
            mcts_manager.run(root_state, root_player)

        return mcts_manager.find_best_action(root_state)

    def fxn(root_state):
        best_move = mcts(root_state, allowed_time, mcts_manager)
        return best_move

    return fxn