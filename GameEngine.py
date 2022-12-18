from Game import Game
from AlphaBeta import AB

class Engine:
    def __init__(self):
        self.game = Game()

    def play(self, agent1, agent2, num_games):
        #Given two agents, set them on the same game and have them play
        
        #hold the initial game board
        hold_board = self.game.board.copy()
        agent1.game = self.game
        agent2.game = self.game
        score = 0
        p1wins = 0
        p2wins = 0
        ties = 0
        for i in range(num_games):
            agent1.game.board = hold_board.copy()
            agent2.game.board = hold_board.copy()
            if i % 2 == 0:
                #agent 1 goes first
                while(True):
                    agent1.find_move(1)
                    #agent1.game.print_board()
                    if(agent1.game.is_terminal_node()):
                        score += agent1.game.game_score()
                        if agent1.game.game_score() == 1:
                            p1wins += 1
                        elif agent1.game.game_score() == -1:
                            p2wins += 1
                        else:
                            ties += 1
                        break
                    agent2.find_move(2)
                    #agent1.game.print_board()
                    if(agent1.game.is_terminal_node()):
                        score += agent1.game.game_score()
                        if agent1.game.game_score() == 1:
                            p1wins += 1
                        elif agent1.game.game_score() == -1:
                            p2wins += 1
                        else:
                            ties += 1
                        break
            else:
                #agent 2 goest first
                while(True):
                    agent2.find_move(2)
                    #agent1.game.print_board()
                    if(agent1.game.is_terminal_node()):
                        score += agent1.game.game_score()
                        if agent1.game.game_score() == 1:
                            p1wins += 1
                        elif agent1.game.game_score() == -1:
                            p2wins += 1
                        else:
                            ties += 1
                        break
                    agent1.find_move(1)
                    #agent1.game.print_board()
                    if(agent1.game.is_terminal_node()):
                        score += agent1.game.game_score()
                        if agent1.game.game_score() == 1:
                            p1wins += 1
                        elif agent1.game.game_score() == -1:
                            p2wins += 1
                        else:
                            ties += 1
                        break
        
        score = score / num_games
        return (str(score) + " P1W: " + str(p1wins) + "  P2W: " + str(p2wins) + "  Ties: " + str(ties))

    def play_and_print(self, agent1, agent2, num_games):
        #Given two agents, set them on the same game and have them play
        
        #hold the initial game board
        hold_board = self.game.board.copy()
        agent1.game = self.game
        agent2.game = self.game
        score = 0
        p1wins = 0
        p2wins = 0
        ties = 0
        for i in range(num_games):
            agent1.game.board = hold_board.copy()
            agent2.game.board = hold_board.copy()
            if i % 2 == 0:
                #agent 1 goes first
                while(True):
                    agent1.find_move(1)
                    agent1.game.print_board()
                    if(agent1.game.is_terminal_node()):
                        score += agent1.game.game_score()
                        if agent1.game.game_score() == 1:
                            p1wins += 1
                        elif agent1.game.game_score() == -1:
                            p2wins += 1
                        else:
                            ties += 1
                        break
                    agent2.find_move(2)
                    agent1.game.print_board()
                    if(agent1.game.is_terminal_node()):
                        score += agent1.game.game_score()
                        if agent1.game.game_score() == 1:
                            p1wins += 1
                        elif agent1.game.game_score() == -1:
                            p2wins += 1
                        else:
                            ties += 1
                        break
            else:
                #agent 2 goest first
                while(True):
                    agent2.find_move(2)
                    agent1.game.print_board()
                    if(agent1.game.is_terminal_node()):
                        score += agent1.game.game_score()
                        if agent1.game.game_score() == 1:
                            p1wins += 1
                        elif agent1.game.game_score() == -1:
                            p2wins += 1
                        else:
                            ties += 1
                        break
                    agent1.find_move(1)
                    agent1.game.print_board()
                    if(agent1.game.is_terminal_node()):
                        score += agent1.game.game_score()
                        if agent1.game.game_score() == 1:
                            p1wins += 1
                        elif agent1.game.game_score() == -1:
                            p2wins += 1
                        else:
                            ties += 1
                        break
        
        score = score / num_games
        return (str(score) + " P1W: " + str(p1wins) + "  P2W: " + str(p2wins) + "  Ties: " + str(ties))


myEngine = Engine()
ab1 = AB(3, "2x1+middle")
ab2 = AB(3, "rand")

print(myEngine.play(ab1, ab2, 1000))
            

