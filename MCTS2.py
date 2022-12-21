import time
import math
import random

from Game import Game

P1_PIECE = 1
P2_PIECE = 2

ROW_COUNT = 6
COL_COUNT = 7

class Node:
    def __init__(self):
        self.state = None

        self.parent = None
        self.moves = []
        self.children = []

        self.visits = 0
        self.reward = 0

class MCTS2:
    def __init__(self):
        self.game = None
        self.piece = P1_PIECE

        self.encoded_state_dict = {} # Encoded state -> Node
        self.current_path = []

    def run_mcts(self, allowed_time):
        # Make a copy of the initial game board for use
        root_state = self.game.board.copy()
        # Encode the root position state into MCTS-enabled state
        root_state_encoded = self.encode_state(root_state)
        # Expand the initial root state
        self.expand(root_state, root_state_encoded)

        # Run MCTS iterations until out of time
        time_end = time.time() + allowed_time
        while time.time() < time_end:
            # Run an iteration
            self.run_iteration(root_state)

        print(len(self.encoded_state_dict))

    def run_iteration(self, root_state):
        # Create a copy of the board to reset to later
        reset_board = self.game.board.copy()

        # Get a state from traversal, then expand/simulate it
        res_state = self.traverse(root_state)
        res_state_encoded = self.encode_state(res_state)
        # self.game.board = res_state
        
        self.expand(res_state, res_state_encoded)
        self.simulate(res_state, res_state_encoded)

        # Reset board
        self.game.board = reset_board
        self.piece = P1_PIECE

    def traverse(self, root_state):
        self.current_path = []
        current_state = root_state

        while True:
            # Encode current state
            current_state_encoded = self.encode_state(current_state)
            # print("current state " + str(current_state_encoded))

            self.current_path.append(current_state_encoded)

            current_state_game = Game()
            current_state_game.board = current_state
            # current_state_game.print_board()
            if current_state_game.is_terminal_node():

            # self.game.print_board()
            # if self.game.is_terminal_node():
                # If the game is over, return the unencoded state
                return current_state
            else:
                # We are at an expanded nonterminal state, find the next state to return
                node = self.encoded_state_dict[current_state_encoded]
                for (index, child_state_encoded) in enumerate(node.children):
                    if child_state_encoded not in self.encoded_state_dict:
                        # Proceed to this unexpanded child state
                        self.game.drop_piece(node.moves[index], self.piece)
                        self.current_path.append(child_state_encoded)
                        self.piece = P2_PIECE if self.piece == P1_PIECE else P1_PIECE
                        # Return the state of the board, which is the child state
                        # print("returning")
                        # print(str(self.game.board))
                        current_state = self.game.board
                        return self.game.board
                    
                # If there are no unexpanded states, use UCB-2 to pick next state, with current state as parent
                [move, current_state] = self.ucb_evaluate(current_state, current_state_encoded, self.piece)
                # Execute the move
                self.game.drop_piece(move, self.piece)

            # Switch the player piece, turn is over
            # issue here? p2 takes too many turns?
            current_state = self.game.board
            self.piece = P2_PIECE if self.piece == P1_PIECE else P1_PIECE

    def expand(self, state, encoded_state):
        if encoded_state not in self.encoded_state_dict:
            # Create new node
            # print("here")
            new_node = Node()

            # Set node unencoded state
            new_node.state = state

            # Populate node's moves
            new_node.moves = self.game.get_valid_locations()
            # Populate node's children (must be in same order as moves?)
            for move in new_node.moves:
                successor_state = self.game.successor(move, self.piece) # self.piece?
                successor_state_encoded = self.encode_state(successor_state)
                new_node.children.append(successor_state_encoded)

            # Update visits
            new_node.visits += 1

            # Update encoded_state_dict
            # print("NOW ENCODING")
            # print(encoded_state)
            # print(new_node.state)
            self.encoded_state_dict[encoded_state] = new_node

    def simulate(self, state, encoded_state):
        # Play a game randomly to the end
        while not self.game.is_terminal_node():
            available_moves = self.game.get_valid_locations()
            selected_move = random.choice(available_moves)
            
            # Drop piece and advance game
            self.game.drop_piece(selected_move, self.piece)
            # Switch piece
            self.piece = P2_PIECE if self.piece == P1_PIECE else P1_PIECE

        # Game over, get payoff and update
        payoff = self.game.game_score()
        self.update(payoff)

    def update(self, payoff):
        # print("current path: " + str(self.current_path))
        for encoded_state in self.current_path:
            node = self.encoded_state_dict[encoded_state]
            node.reward += payoff
            node.visits += 1

    def encode_state(self, state):
        # Convert a numpy state into a string
        # print(state)
        encoded_string = ""
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                encoded_string += str(state[i][j])
                encoded_string += " "
        return encoded_string

    def ucb_evaluate(self, parent_state, parent_state_encoded, parent_state_player):
        best_ucb_score = 0
        best_ucb_move = None
        best_ucb_state = None

        if parent_state_player == 1:
            best_ucb_score = float('-inf')
        else:
            best_ucb_score = float('inf')

        node = self.encoded_state_dict[parent_state_encoded]
        for (index, child_state_encoded) in enumerate(node.children):
            # Get the move that obtains this child state
            move_to_child = node.moves[index]

            # Encode the child state and score it
            child_state_score = self.ucb_score(parent_state_encoded, parent_state_player, child_state_encoded)
            if parent_state_player == 1:
                if child_state_score >= best_ucb_score:
                    best_ucb_score = child_state_score
                    best_ucb_move = move_to_child
                    best_ucb_state = child_state_encoded
            else:
                if child_state_score <= best_ucb_score:
                    best_ucb_score = child_state_score
                    best_ucb_move = move_to_child
                    best_ucb_state = child_state_encoded

        return [best_ucb_move, self.encoded_state_dict[best_ucb_state].state]

    def ucb_score(self, parent_state_encoded, parent_state_player, child_state_encoded):
        parent_node = self.encoded_state_dict[parent_state_encoded]
        child_node = self.encoded_state_dict[child_state_encoded]
        parent_state_visits = parent_node.visits
        child_state_reward = child_node.reward
        child_state_visits = child_node.visits

        if child_state_visits == 0:
            return 0

        term1 = child_state_reward / child_state_visits
        term2 = math.sqrt( (2 * math.log(parent_state_visits)) / child_state_visits )

        if parent_state_player == 1:
            return (term1 + term2)
        else:
            return (term1 - term2)

    def find_move(self, player):
        # Get state from current board and encode
        parent_state = self.game.board
        parent_state_encoded = self.encode_state(parent_state)

        # Check to make sure parent state is in the dictionary, if not, play randomly
        if parent_state_encoded not in self.encoded_state_dict:
            # Get a random action
            parent_game = Game()
            parent_game.board = parent_state
            valid_actions = parent_game.get_valid_locations()
            self.game.drop_piece(random.choice(valid_actions), player)
            return

        parent_node = self.encoded_state_dict[parent_state_encoded]
        
        best_score = 0
        best_action = None

        if player == 1:
            best_score = float("-inf")
        else:
            best_score = float("inf")

        for index, child_state_encoded in enumerate(parent_node.children):
            if child_state_encoded in self.encoded_state_dict:
                child_node = self.encoded_state_dict[child_state_encoded]
                child_state_score = child_node.reward / child_node.visits

                if player == 1:
                    if child_state_score > best_score:
                        best_score = child_state_score
                        best_action = parent_node.moves[index]
                else:
                    if child_state_score < best_score:
                        best_score = child_state_score
                        best_action = parent_node.moves[index]
            else:
                # do the same thing
                # Get a random action
                parent_game = Game()
                parent_game.board = parent_state
                valid_actions = parent_game.get_valid_locations()
                self.game.drop_piece(random.choice(valid_actions), player)
                return

        # Drop piece according to best move
        self.game.drop_piece(best_action, player)