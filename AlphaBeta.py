from Game import Game

P1_PIECE = 1
P2_PIECE = 2

ROW_COUNT = 6
COL_COUNT = 7


myGame = Game()
myGame.print_board()
print(myGame.get_valid_locations())
myGame.drop_piece(2,1)
myGame.drop_piece(2,1)
myGame.drop_piece(2,1)
myGame.drop_piece(2,1)
myGame.drop_piece(2,1)
myGame.drop_piece(2,1)
myGame.drop_piece(2,1)
myGame.drop_piece(2,1)
myGame.drop_piece(2,1)
myGame.print_board()