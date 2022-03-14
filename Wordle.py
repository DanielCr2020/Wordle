'''
Wordle.py
Wordle implemented in Python

Lowercase letters represent letters that are correct, but not in the correct
location.

Uppercase letters represent letters that are correct and in the correct location.

Underscores represent an incorrect letter.
'''
import random

file=open("words.txt")
data=file.readlines()

lines=0

for line in data:
    lines+=1

file.close()

randWord=data[random.randrange(0,2310)]
randWord=randWord.replace("\n","")
validGuesses=data[random.randrange(0,lines)]
validGuesses=validGuesses.replace("\n","")


'''
use currLine to build string. Replace each underscore with a letter
'''


def play():
    randWord=data[random.randrange(0,2310)]
    randWord=randWord.replace("\n","")
    guesses=0
    guessed=False
    output=""
    temp=str(randWord)
    while(guesses<6 and guessed==False):
        guess=input("Guess "+str(guesses+1)+"/6: ")
        while guess+"\n" not in data:
            guess=input("'"+guess+"'"+ " is not in word list: ")
        guesses+=1
        currLine="_ _ _ _ _"
        if guess==randWord:
            for j in range(len(guess)):
                currLine=currLine.replace(currLine[j*2],guess[j].upper(),1)
                currLine=currLine[:j*2]+guess[j].upper()+currLine[(j*2)+1:]
            guessed=True
            output+=currLine
            break
        for i in range(5):
            if guess[i]==randWord[i]:
                currLine=currLine[:i*2]+guess[i].upper()+currLine[(i*2)+1:]
                temp=temp.replace(guess[i],'',1)
        for j in range(5):
            if guess[j] in temp:
                if currLine[j*2]=="_":
                    currLine=currLine[:j*2]+guess[j].lower()+currLine[(j*2)+1:]
                    temp=temp.replace(guess[j],'',1)
        output+=currLine+"\n"
        temp=randWord
        print(output)

    #print(output)

    if guessed==False:
        print(randWord)
    else:
        print(output)
        print("Congratulations! You guessed the word "+"'"+randWord+"' "+"in "+
        str(guesses)+(" guess!" if guesses==1 else " guesses!"))

play()
print("\nType 'play()' to play. A new random word will be chosen each time.")
