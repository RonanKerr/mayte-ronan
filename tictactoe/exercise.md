# TicTacToe 
Implement the game of Tic Tac Toe in python, where a human can play against the computer.

Make sure your classes:
 * use appropriate fabrication to minimise coupling
 * have a single responsibility. For example, displaying the game, modelling the game, the ai logic and running the game are all separate responsibilities
 * have good test coverage, especially for your methods with no i/o, as these are easy to test. 

## Part 1 -- Model
Implement your model for tic-tac-toe.
In this model, you should:
* Define methods that are useful in interpreting the state, and making moves to manipulate the state (if it is mutable), or create new states if it is immutable.
* Validate that moves made are valid, and throw an invalid move exception (see part 2) if they are not

Hints
* All functions in your model file should be pure (no i/o or global variables) -- the model is not concerned about how the game is played
* Consider which data structures are best suited to model each part of the game
* Try to make an elegant function to determine if the game is over
* Think carefully about function and variable naming


## Part 2 -- Exception
Define your own invalid move exception in the file `tic_tac_toe_move_exception.py`

## Part 3 -- Tests
Define tests to cover every function in your model.

## Part 4 -- Game
Define the logic to play the game through a terminal in `tic_tac_toe_game.py`

The computer player logic and rendering code can be placed in this file or another if you wish.

It is not required to make the computer player intelligent, but it should always make a valid move.


# Optional Parts
## Persistence
Make it possible to store the state of a game to a file, and resume it later. 

## n*n tic-tac-toe
Make it possible to run your game for any number of cells rather only 3X3 e.g., 5X5, 7X7 etc. you can take the n input on starting the game

## Master A.I.
Write an A.I. that plays the [perfect game](https://en.wikipedia.org/wiki/Solved_game#Perfect_play)