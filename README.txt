Usage:

./Connect4 [engine1] [engine2]

For an Alpha-Beta engine:

a [depth] [heuristic] <-- number from 1 to 8 - 1 is the best heuristic, 8 is random

For a Monte-Carlo engine:

m [time] <-- time given for Monte-Carlo training


Examples:

./Connect4 a 3 1 a 5 2
./Connect4 a 3 1 m 10
./Connect4 m 10 a 5 2
./Connect4 m 10 m 20
