# Wordle
Simple, functional Wordle clode made in Python


Wordle clone in python that reads from a file a list of words and picks a random one. 

The Wordle.py file must be in the same directory as "words.txt" in order to function properly.

Lowercase letters indicate a correct letter in an incorrect location. 
Uppercase letters indicate a correct letter in the correct location.
Underscores indicate an incorrect letter.

To run, open the python file and run it. The game will give you 6 guesses to guess a 5 letter word.

After the game is over, type play() to play again.

First, a random word is selected. A temp string (currLine) for each line is initalized to underscores the characters are replaced as necessary. An output string is also initialized to empty. If the word is guessed, the game ends and it reports how many guesses it took. Otherwise, if the letter is correct and in the correct place, the currLine string at that index is replaced with a capital of the correct letter. That letter is then removed from the temp string, a local copy of the randomWord string used for letter tracking. After it runs through the entire string once, replacing letters as necssary, it runs through it again for lowercase letters. At this point, we know that the only letters left are correct and in the wrong place, or incorrect. The program checks if each letter is in the temp string (the correctly placed letters have already been removed). If they are, it replaces the underscores in currLine with lowercase letters. The index of the letter in currLine matches that of the guess string. The string is only updated if there is an underscore that needs to be replaced. This fixes incorrect replacement. After that is done, currLine is appended to the output, which is output after each guess, to show the progress of guesses.

Finally, if the user does not guess the random word, it is revealed. Otherwise, the game congratulates them and says the number of guesses they took. 



