import random
import time
import winsound

# List of words for the game
words = ["Goku", "Claymore", "Hiking", "Protein", "Astolfo", "Sigma",
         "Genji", "Intervention", "Insomnia", "Zimmerman", "Paper", "Bread",
         "Widowmaker", "Tracer", "Kerrigan", "Zeratul", "Rai", "Fennix",
         "Raynor", "Kwantlen"]

# List of messages for correct and incorrect guesses
correct_guess_messages = ["You're on a roll brother!", "Great guess traveller!", "You're on firehan!"]
incorrect_guess_messages = ["Eeeerr, try again!", "Better luck next guess buddy!", "Oops, you can do better champ!"]

# List of hangman pictures
hangman_pics = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']

# Function to select a random word from the list of words
def choose_word():
    while True:
        word = random.choice(words)
        if word not in ["Rai", "Zimmerman"]:
            return word

# Function to display the hangman picture
def display_hangman(guesses):
    print(hangman_pics[guesses])

# Function to display the word with underscores for unguessed letters
def display_word(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

# Function to get a valid letter guess from the user
def get_letter_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter only one letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        else:
            return guess

# Function to check if the guessed letter is in the word
def check_guess(guess, word, guessed_letters):
    if guess in word:
        guessed_letters.add(guess)
        print(random.choice(correct_guess_messages))
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    else:
        print(random.choice(incorrect_guess_messages))
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        display_hangman(len(guessed_letters))
    time.sleep(1)

# Function to check if the game is won
def check_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Function to play the game
def play_game():
    print("Let's play Hangman!")
    word = choose_word()
    guessed_letters = set()
    guesses_left = len(hangman_pics) - 1
    
    while guesses_left > 0:
        display_hangman(len(guessed_letters))
        display_word(word, guessed_letters)
        guess = get_letter_guess(guessed_letters)
        check_guess(guess, word, guessed_letters)
        if check_win(word, guessed_letters):
            print("You win!")
            play_sound("win")
            break
        guesses_left -= 1
        time.sleep(1)
    
    if not check_win(word, guessed_letters):
        print(f"Sorry, you lose! The word was '{word}'.")
        play_sound("lose")
    
    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")
        play_sound("end")

# Call the play_game function to start the game
play_game()
