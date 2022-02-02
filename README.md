# Checkers AI
 
### A simple checkers game played on a square checker board (often 8 x 8) which allows two players to play against each other or one player to play against an AI opponent.

This project was developed as a final project for CPSC-481 Artifical Intelligence class.
- It utilizes the min-max algorithm which in turn uses a depth-first search algorithm for the AI opponent.
- The AI difficulty level can be adjusted by utilizing an adjustable depth-limited search.
- Players can also modify the gameboard to play any size checkers board they want! (Although the bigger the board is the longer the AI will take to find the right move).
-- To change board size go to `constants.py` file and change SIZE to any even value you want

The project was developed using python and the UI was constructed using the pygames and tkinter library.

## Game play:
When a player clicks on a piece, the green dots will show the player all the valid moves for that piece as shown below.
========
![8 x 8 Checkers Board](https://github.com/belhaghassan/Checkers-AI/blob/main/resources/board.png "Checker Board Gameplay")


To play this repo game of checkers download the repo and install pygames and tkinter libraries:

```
git clone https://github.com/belhaghassan/Checkers-AI.git
```
```
pip install pygame
```
```
cd /Checkers-AI
```
```
python main.py
```

