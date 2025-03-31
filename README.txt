Pedro Paulo da Silva Dutra Pernes - RU: 4677680

Tetris Game

Overview:
This is a simple implementation of the classic Tetris game using Python and the Pygame library. The game features the basic mechanics of Tetris, where the player controls falling tetrominoes and must rotate, move, and arrange them to complete lines and score points.

Features:
- Piece Rotation: Rotate pieces using the Spacebar key.
- Movement: Move pieces left, right, and down using the arrow keys.
- Game Over: The game ends when the tetrominoes stack up to the top of the screen.
- Score: The score increases when a line is cleared.
- Game Speed: The speed of the falling pieces can be controlled by the game's frame rate.

Requirements:
To run this project, you need Python 3.x and the Pygame library installed.

Install Python 3:
If you don't have Python 3 installed, download and install it from the official website: https://www.python.org/downloads/

Install Pygame:
You can install the Pygame library by running the following command:

    pip install pygame

Or, you can use the `requirements.txt` file to install all dependencies at once:

1. Install the required libraries using the following command:

    pip install -r requirements.txt

How to Run:
1. Clone the repository:

    git clone https://github.com/PedroDutra86/tetris-game.git

2. Navigate to the project directory:

    cd tetris-game

3. Run the game:

    python main.py

Controls:
- Arrow Left: Move the current tetromino left.
- Arrow Right: Move the current tetromino right.
- Arrow Down: Move the current tetromino down.
- Spacebar: Rotate the current tetromino.

File Structure:
tetris/
├── main.py           # Main game logic and entry point
├── constants.py      # Game constants (e.g., colors, screen dimensions)
├── game.py           # Game-related functions (e.g., rotation, collision check)
├── graphics.py       # Functions for rendering game objects
├── README.txt        # This file
└── requirements.txt  # List of required dependencies for the project

