import time
import math
import random
import numpy
from Game import Game

P1_PIECE = 1
P2_PIECE = 2

ROW_COUNT = 6
COL_COUNT = 7

class MCTS:
    def __init__(self):
        self.game = None
        self.piece = P1_PIECE
        # Array for current traversal path
        self.current_path = []
        # Dictionary mapping { State: [Reward, Num Visits, Actions, Child States] }
        self.state_dict = {}
        # Dictionary mapping { State: [All Possible Next Actions] }
        self.action_dict = {}
        # Dictionary mapping { State: [All Possible Next States] }
        self.children_dict = {}

    # In the allowed time, generate an MCTS tree
    def run_mcts(self, allowed_time):
        # Copy the initial board state and expand it
        root_state = self.game.board.copy()
        root_state_encoded = self.encode_array(root_state)
        self.expand(root_state_encoded)

        time_end = time.time() + allowed_time
        while time.time() < time_end:
            # Run an iteration
            self.run_iteration(root_state)
            # Reset the board
            self.game.board = root_state

        #print(self.state_dict)

    # Does 1 run through the MCTS tree
    def run_iteration(self, root_state):
        res_state = self.traverse(root_state)
        self.expand(res_state)
        self.simulate(res_state)

    def traverse(self, root_state):
        self.current_path = []
        current_state = root_state
        while True:
            # Encode current state
            current_state = self.encode_array(current_state)

            self.current_path.append(current_state)
            if self.game.is_terminal_node():
                return current_state
            else:
                available_next_states = self.state_dict[current_state][3]
                for next_state in available_next_states:
                    if next_state not in self.state_dict:
                        self.current_path.append(next_state)
                        return next_state
                # Run UCB-2
                current_state = self.ucb_evaluate(current_state, self.piece)
            # Switch player piece
            self.piece = P2_PIECE if self.piece == P1_PIECE else P2_PIECE

    def expand(self, state):
        if state not in self.state_dict:
            self.state_dict[state] = [0, 0, [], []]
            self.get_child_actions_and_states(state)

    def simulate(self, state):
        hold_board = self.game.board.copy()
        while not self.game.is_terminal_node():
            # Get a list of available columns (aka moves/actions) to drop a piece into
            available_actions = self.game.get_valid_locations()
            selected_action = random.choice(available_actions)
            # Drop piece and advance game
            self.game.drop_piece(selected_action, self.piece)
            # Switch piece
            self.piece = P2_PIECE if self.piece == P1_PIECE else P2_PIECE
        

        # Get payoff and update MCTS
        payoff = self.game.game_score()
        self.update(payoff)
        self.game.board = hold_board.copy()

    def update(self, payoff):
        for state in self.current_path:
            entry = self.state_dict[state]
            entry[0] += payoff
            entry[1] += 1

    def get_child_actions_and_states(self, state):
        available_actions = self.game.get_valid_locations()
        for action in available_actions:
            self.state_dict[state][2].append(action)
            # Need to change piece depending on who's turn it is
            successor_state = self.game.successor(action, self.piece)
            self.state_dict[state][3].append(self.encode_array(successor_state))
            #self.state_dict[self.encode_array(successor_state)] = [0,0,[],[]]

    def ucb_evaluate(self, parent_state, parent_state_player):
        best_ucb_score = 0
        best_ucb_score = None

        if parent_state_player == 1:
            best_ucb_score = float('-inf')
        else:
            best_ucb_score = float('inf')

        for child_state in self.state_dict[parent_state][3]:
            child_state_score = self.ucb_score(parent_state, parent_state_player, child_state)
            if parent_state_player == 1:
                if child_state_score >= best_ucb_score:
                    best_ucb_score = child_state_score
                    best_ucb_state = child_state
            else:
                if child_state_score <= best_ucb_score:
                    best_ucb_score = child_state_score
                    best_ucb_state = child_state

        return best_ucb_state

    def ucb_score(self, parent_state, parent_state_player, child_state):
        parent_state_info = self.state_dict[parent_state]
        child_state_info = self.state_dict[child_state]
        parent_state_visits = parent_state_info[1]
        child_state_reward = child_state_info[0]
        child_state_visits = child_state_info[1]

        if child_state_visits == 0:
            return 0

        term1 = child_state_reward / child_state_visits
        term2 = math.sqrt( (2 * math.log(parent_state_visits)) / child_state_visits )

        if parent_state_player == 1:
            return (term1 + term2)
        else:
            return (term1 - term2)

    def encode_array(self, arr):
        encoded_res = []
        # rows = len(arr)
        # cols = len(arr[0])
        for i in range(ROW_COUNT): #rows):
            for j in range(COL_COUNT): #cols):
                encoded_res.append(arr[i][j])
        return str(encoded_res)

    # Given a state and a player to move, finds the best move and drops piece
    def find_move(self, player):
        # print(self.state_dict)
        state = self.game.board
        encoded_state = self.encode_array(state)
        best_score = 0
        best_action = None

        if player == 1:
            best_score = float("-inf")
        else:
            best_score = float("inf")

        # print("state dict")
        # print(encoded_state)
        # print(self.state_dict[encoded_state][3])
        possible_actions = []

        for index, next_state in enumerate(self.state_dict[encoded_state][3]):
            if next_state in self.state_dict.keys():
                next_state_score = self.state_dict[encoded_state][0] / self.state_dict[next_state][1]
                if player == 1:
                    if next_state_score > best_score:
                        best_score = next_state_score
                        best_action = self.state_dict[encoded_state][2][index]
                else:
                    if next_state_score < best_score:
                        best_score = next_state_score
                        best_action = self.state_dict[encoded_state][2][index]
            else:
                #possible_actions.append(self.state_dict[encoded_state][2][index])
                best_action = self.state_dict[encoded_state][2][index]
        
        if len(possible_actions) > 0:
            best_action = random.choice(possible_actions)

        # Drop piece according to best move
        # print("best action?")
        self.game.drop_piece(best_action, player)