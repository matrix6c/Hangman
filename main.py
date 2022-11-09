import random
import hangman_word
import hangman_art



# get a random word from word list
chosen_word = random.choice(hangman_word.word_list)
print(hangman_art.logo)
# for testing
# print(f"chosen word is {chosen_word}")

display = []

# count length of letters in chosen word
word_length = len(chosen_word)

for char in range(word_length):
    display += "_"
  
#Join all the elements in the list and turn it into a String.
print(f"{' '.join(display)} \n")

# declare if game should continue
end_of_game = False
lives = 7
guessed = []

# check if game should continue
while not end_of_game:
    # user guess
    guess = input("Guess a letter: ").lower()
    
    # print(f"You guessed {guessed}")
    for position in range(word_length):
        letter = chosen_word[position]

        # replace dash with guessed letters
        if letter == guess:
            display[position] = letter

    # check if user guessed the same letter twice
    if guess in guessed:
        print(f"You have guessed {guess}, please guess another letter")

    # check if guessed letter is in chosen word
    elif guess not in chosen_word:
        if lives > 0:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            
        if lives == 0 :
            print("you lose")
            end_of_game = True

    # accounting for total letters user have guessed
    guessed +=  guess
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # show user status of life
    print(hangman_art.stages[lives])
    
    # check  if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("you win")