Connect4:
	echo "#!/bin/bash" > Connect4
	echo "python3 GameEngine.py \"\$$@\"" >> Connect4
	chmod u+x Connect4