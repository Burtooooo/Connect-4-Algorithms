Project Members: David Metrick, John Wahlig, Burton Lyng-Olsen
Project Follow-On Video (New): https://youtu.be/W_eniNkZCg0

Usage:

./Connect4 [iterations] [engine1] [engine2]

OR: To run example tests, which is a Monte Carlo agent with 30 seconds to train versus each heuristic of alpha-beta
with depth 3,
run: ./Connect4 testscript

iterations: Number of games to play

For an Alpha-Beta engine:

a [depth] [heuristic] <-- number from 1 to 8 - 1 is the best heuristic, 8 is random

For a Monte-Carlo engine:

m [time] <-- time given for Monte-Carlo training


Examples:

./Connect4 10 a 3 1 a 5 2
./Connect4 10 a 3 1 m 10
./Connect4 20 m 10 a 5 2
./Connect4 20 m 10 m 20

To interpret the results, the first number can be read as the expected value of a game for Player 1. This number ranges from -1.0 to 1.0.
The number following P1W is the number of wins for Player 1 over the amount of iterations run,
whereas the number following P2W is the number of wins for Player 2 over the amout of iterations run.
This is all followed by the number of ties encountered in the iterations run.

NOTE: The heuristics involving the middle can turn into deterministic strategies depending on what the game is, so it might get some unusual
results when matched up against the Monte-Carlo agent.