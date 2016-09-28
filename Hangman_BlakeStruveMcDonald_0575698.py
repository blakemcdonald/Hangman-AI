#Name: Blake Struve-McDonald
#Student_ID: 0575698
#Date: 9/28/2016
import random
words = ["computer","science","university","interesting","word","president","random","hard","think","soft","visual","studio","community","list","vancouver","canada","denmark","sweden","norway","battlefield","airplane","helicopter","connect","disconnect","incorrect","correct","wrecked","mate","fate","fight","bright","music","electronic","classical","alternative","calculus","relation","database","software","manitoba","jupiter","arena","hockey","explore","provide","quality","almost","done","amount","please"]
hangPatterns = ['''
  x-----x 
  |     |
  |     
  |     
  |
  |
--x-----''', '''
  x-----x
  |     |
  |     O
  |    
  |     
  |    
  |
--x-----''', '''
  x-----x
  |     |
  |     O
  |     |
  |     
  |    
  |
--x-----''', '''
  x-----x
  |     |
  |     O
  |     |
  |     |
  |    
  |
--x-----''', '''
  x-----x
  |     |
  |     O
  |    \|
  |     |
  |    
  |
--x-----''', '''
  x-----x
  |     |
  |     O
  |    \|/
  |     |
  |    
  |
--x-----''', '''
  x-----x
  |     |
  |     O
  |    \|/
  |     |
  |    / 
  |
--x-----''', '''
  x-----x
  |     |
  |     O
  |    \|/
  |     |
  |    / \\
  |
--x-----''']

def randomWord():
    return words[random.randint(0,len(words) - 1)]

incorrectLetters = ""        #keeps track of incorrect letters guessed
correctLetters = ""          #keeps track of correct letters guessed
play = True
guess = ""
correct = 0
index = 0

def printPattern(guesses):
    print hangPatterns[guesses]

randomWord = randomWord()
hiddenWord = list("")               #needs to be a list so the underscores in the middle of the word can be changed to letters
i = 0
while i < len(randomWord):
    hiddenWord += "_"               #makes a list of underscores the size of the randomword
    i += 1

print("HANGMAN GAME")       
print("------------")

while play == True:
    
    printPattern(len(incorrectLetters))                 #decides which pattern to print depending on how many incorrect guesses youve made
    print "Word: " + "".join(hiddenWord)                #how to print a list as a string
    print "Incorrect letters: " + incorrectLetters
    guess = raw_input("Guess a letter (1 for guessing whole word): ")       #input for guess

    if guess == '1':
       guessWord = raw_input("Guess the word: ")                            #if user enters '1' they are able to guess the whole word, if they get it wrong they lose the whole game
       if randomWord.find(guessWord) > -1:
           play = False
           print "You have correctly guessed the word!"
       else:
           print "You have incorrectly guessed the word, you lose..."
           print hangPatterns[7]
           play = False
    elif len(guess) > 1:
        print "Just guess a single character"               #error trap for more than one character
    elif correctLetters.find(guess) > -1:
        print "You've already guessed " + guess             #error trap for already guessed character
    else:
        if randomWord.find(guess) > -1:
            correctLetters += guess
            print "Found " + guess
            index = 0       #index needs to be reset each time
            while index < len(hiddenWord):                    #This is for more than one occurence of the letter in the hidden word
                index = randomWord.find(guess, index)
                if index == -1:
                    break
                hiddenWord[index] = guess
                correct += 1                                  #increases correct letters guessed
                index += 1
        else:
            incorrectLetters += guess                         #not including an error trap for already guessed incorrect letters, it is the players' responsibility to not be an idiot. So he can choose 'g' twice if he wants and he will add to the hangman a second time               
            print "Did not find " + guess
                

    if len(incorrectLetters) == 7:              #lose check
        print hangPatterns[7]
        print "You lose..."
        play = False
    elif correct == len(randomWord):                          #win check
        print "You win!"
        play = False
    
    if play == False:
        again = raw_input("Would you like to play again? (y/n): ")          #option to play again or not
        if again.lower() == 'y':
            print "RESETING GAME"

            randomWord = words[random.randint(0,len(words) - 1)]
            hiddenWord = list("")
            i = 0
            while i < len(randomWord):
                hiddenWord += "_"
                i += 1

            incorrectLetters = ""        #keeps track of incorrect letters guessed
            correctLetters = ""          #keeps track of correct letters guessed
            play = True
            guess = ""
            correct = 0
