
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman word-guessing game using Python strings, loops, user input, and random selection.

## 📝 Tasks

### 🛠️ Create the Game State

#### Description
Set up the secret word and variables needed to track the player's guesses and remaining attempts.

#### Requirements
Completed program should:

- Randomly select one word from the predefined `words` list
- Initialize a collection that records the player's guessed letters
- Set the number of incorrect guesses to zero
- Set a maximum number of incorrect guesses
- Display the secret word as underscores with one underscore for each letter


### 🛠️ Run the Hangman Game

#### Description
Create a game loop that accepts guesses, updates the game state, and determines whether the player wins or loses.

#### Requirements
Completed program should:

- Accept one letter guess from the player at a time
- Check whether the guessed letter appears in the secret word
- Reveal correctly guessed letters in the displayed word
- Track incorrect guesses and remaining attempts
- End when the player guesses every letter or exhausts the allowed attempts
- Display a clear win or lose message
