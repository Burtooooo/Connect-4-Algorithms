from Game import Game
from AlphaBeta import AB
from MCTS import MCTS
import sys

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
        self.game.board = hold_board.copy()
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
        self.game.board = hold_board.copy()
        
        score = score / num_games
        
        return (str(score) + " P1W: " + str(p1wins) + "  P2W: " + str(p2wins) + "  Ties: " + str(ties))


myEngine = Engine()
# ab1 = AB(3, "2x1+middle")
# ab2 = AB(3, "rand")
# mcts1 = MCTS()
# mcts2 = MCTS()
# mcts1.game = myEngine.game
# mcts2.game = myEngine.game
# mcts1.run_mcts(1)
# print("mcts2 running now")
# mcts2.run_mcts(1)
# print(myEngine.play(mcts1, mcts2, 10))
# print(myEngine.play(mcts2, mcts1, 10))

if sys.argv[1] == "testscript":
    mcts_engine = MCTS()
    mcts_engine.game = myEngine.game
    mcts_engine.run_mcts(30)

    ab_engine1 = AB(3, "2x1+middle")
    ab_engine2 = AB(3, "3row+middle")
    ab_engine3 = AB(3, "middle")
    ab_engine4 = AB(3, "center")
    ab_engine5 = AB(3, "2x1")
    ab_engine6 = AB(3, "3inrow")
    ab_engine7 = AB(3, "touching")
    ab_engine8 = AB(3, "rand")

    print(myEngine.play(mcts_engine, ab_engine1, 10))
    print(myEngine.play(mcts_engine, ab_engine2, 10))
    print(myEngine.play(mcts_engine, ab_engine3, 10))
    print(myEngine.play(mcts_engine, ab_engine4, 10))
    print(myEngine.play(mcts_engine, ab_engine5, 10))
    print(myEngine.play(mcts_engine, ab_engine6, 10))
    print(myEngine.play(mcts_engine, ab_engine7, 10))
    print(myEngine.play(mcts_engine, ab_engine8, 10))

else:
    iterations = int(sys.argv[1])
    if sys.argv[2] == "m":
        engine1 = MCTS()
        engine1.game = myEngine.game
        engine1.run_mcts(int(sys.argv[3]))

        if sys.argv[4] == "m":
            engine2 = MCTS()
            engine2.game = myEngine.game
            engine2.run_mcts(int(sys.argv[5]))
        
        elif sys.argv[4] == "a":
            depth = int(sys.argv[5])
            if int(sys.argv[5]) == 1:
                heur = "2x1+middle"
            elif int(sys.argv[5]) == 2:
                heur = "3row+middle"
            elif int(sys.argv[5]) == 3:
                heur = "middle"
            elif int(sys.argv[5]) == 4:
                heur = "center"
            elif int(sys.argv[5]) == 5:
                heur = "2x1"
            elif int(sys.argv[5]) == 6:
                heur = "3inrow"
            elif int(sys.argv[5]) == 7:
                heur = "touching"
            elif int(sys.argv[5]) == 8:
                heur = "rand"
            else:
                quit("See README for usage")
            engine2 = AB(depth, heur)

        else:
            quit("See README for usage")
    #3inarow, 3row+middle, rand, touching, middle, center, 2x1, 2x1+middle
    elif sys.argv[2] == "a":
        depth = int(sys.argv[3])
        if int(sys.argv[4]) == 1:
            heur = "2x1+middle"
        elif int(sys.argv[4]) == 2:
            heur = "3row+middle"
        elif int(sys.argv[4]) == 3:
            heur = "middle"
        elif int(sys.argv[4]) == 4:
            heur = "center"
        elif int(sys.argv[4]) == 5:
            heur = "2x1"
        elif int(sys.argv[4]) == 6:
            heur = "3inrow"
        elif int(sys.argv[4]) == 7:
            heur = "touching"
        elif int(sys.argv[4]) == 8:
            heur = "rand"
        engine1 = AB(depth, heur)

        if sys.argv[5] == "m":
            engine2 = MCTS()
            engine2.game = myEngine.game
            engine2.run_mcts(int(sys.argv[6]))
        
        elif sys.argv[5] == "a":
            depth = int(sys.argv[6])
            if int(sys.argv[7]) == 1:
                heur = "2x1+middle"
            elif int(sys.argv[7]) == 2:
                heur = "3row+middle"
            elif int(sys.argv[7]) == 3:
                heur = "middle"
            elif int(sys.argv[7]) == 4:
                heur = "center"
            elif int(sys.argv[7]) == 5:
                heur = "2x1"
            elif int(sys.argv[7]) == 6:
                heur = "3inrow"
            elif int(sys.argv[7]) == 7:
                heur = "touching"
            elif int(sys.argv[7]) == 8:
                heur = "rand"
            engine2 = AB(depth, heur)
        
        else:
            quit("See README for usage")
    else:
        quit("See README for usage")

    print(myEngine.play(engine1, engine2, iterations))



    # print(myEngine.play(ab1, ab2, 20))
    # print(myEngine.play(ab2, ab1, 20))