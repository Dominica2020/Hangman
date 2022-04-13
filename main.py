#Step 5
import random
import hangman_words
#from hangman_art import stages, logo
import hangman_art

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []

for blank in chosen_word:
    display.append("_")

while "_" in display:
    guess = input("Guess a letter: ").lower()

    hangman_words.divider()

    if guess in display:
        print("")
        print(f"You've already guessed '{guess}'.")

    #Check guessed letter
    for index in range(word_length):
        if guess == chosen_word[index]:
            display[index] = guess

    #Join all the elements in the list and turn it into a String.
    print("")
    print("".join(display))
    print("")
    
    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")
    
    print("")
    print(f"Lives: {lives}")
    print(hangman_art.stages[lives])
    
    if lives == 0:
        print("You lose.")
        break
         
    if "_" not in display:
        print("You win!")
        break
